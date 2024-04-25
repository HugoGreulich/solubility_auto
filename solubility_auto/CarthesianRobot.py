import serial
import time
import re
import configparser

config_path = r'C:\Users\Hugo Greulich Mayor\Documents\GitHub\solubility_auto\config\anycubic_kobra_neo_2.ini' # check pour plus simple

config = configparser.ConfigParser()
config.read(config_path)
dim_x = config.getint('DEFAULT', 'dim_x')
dim_y = config.getint('DEFAULT', 'dim_y')
dim_z = config.getint('DEFAULT', 'dim_z')
A1_x = config.getint('SETTINGS', 'A1_x')
A1_y = config.getint('SETTINGS', 'A1_y')
pos_low = config.getint('SETTINGS', 'pos_low')
pos_high = config.getint('SETTINGS', 'pos_high')
columns = config.getint('SETTINGS', 'columns')
rows = config.getint('SETTINGS', 'rows')

class CarthesianRobot:
    def __init__(self):
        self.serial = None
        self.feedrate = 1500  # Set default feedrate

    def connect_serial(self, port, baudrate):
        """
        Establishes a serial connection using specified settings.
        """
        self.serial = serial.Serial(port, baudrate, timeout=None)
        time.sleep(2)  # Wait for connection to establish
        print(f"Connected to {port} at {baudrate} baud rate.")

    def disconnect_serial(self):
        if self.serial:
            self.serial.close()
            print("Connection closed.")

    def send_gcode(self, command):
        """
        Send a G-code command to the printer and read the response.
        """
        print(f"Sending: {command}")
        self.serial.write((command + '\n').encode())
        response = self.serial.readline().decode().strip()
        print("Printer response:", response)

    def get_current_position(self):
        self.serial.write('M114 \n'.encode())
        response = self.serial.readline().decode().strip()
        pattern = re.compile(r'X:([\d.]+) Y:([\d.]+) Z:([\d.]+)')
        match = pattern.search(response)
        if match:
            x_value = float(match.group(1))
            y_value = float(match.group(2))
            z_value = float(match.group(3))
            current_position = [x_value, y_value, z_value]
            print(current_position)
            return current_position
        else:
            print("No X, Y, and Z values found in the response string.")

    def move_relative(self, x=None, y=None, z=None):
        current_positions = self.get_current_position()
        increments = [float(x), float(y), float(z)]
        new_positions = [position + increment for position, increment in zip(current_positions, increments)]
        if 0 < new_positions[0] < dim_x and 0 < new_positions[1] < dim_y and 0 < new_positions[2] < dim_z:
            self.send_gcode("G91")  # Set to relative positioning
            self.move_axis(x, y, z)
        else:
            print("Movement out of bounds")

    def move_relative(self, x=None, y=None, z=None):  # Le check 'is next move in range' me pose beaucoup de galères. Pour l'instant j'utilise ça.
        self.send_gcode("G91")
        self.move_axis(x, y, z)
        self.send_gcode("M400")

    def move_absolute(self, x=None, y=None, z=None):
        self.send_gcode("G90")  # Set to absolute positioning
        self.move_axis(x, y, z)
        self.send_gcode("M400")

    def move_up(self):
        self.move_absolute(None, None, pos_high)  # Set z-axis as desired to get pipette out of vial

    def move_down(self):
        self.move_absolute(None, None, pos_low)  # Here I defined the height at which pipette should be lowered to in the .ini file

    def move_to_rest(self):
        self.move_absolute(None, None, dim_z)
        self.move_absolute(dim_x, dim_y, None)

    def move_increase_nbr(self):
        self.move_up()
        self.move_relative(0, -9, 0)
        self.move_down()

    def move_decrease_nbr(self):
        self.move_up()
        self.move_relative(0, 9, 0)
        self.move_down()

    def move_increase_let(self):
        self.move_up()
        self.move_relative(-9, 0, 0)
        self.move_down()

    def move_axis(self, x=None, y=None, z=None):
        command = "G1"
        if x is not None:
            command += f" X{x}"
        if y is not None:
            command += f" Y{y}"
        if z is not None:
            command += f" Z{z}"
        command += f" F{self.feedrate}"
        self.send_gcode(command)

    def home_axis(self, axis):
        if axis not in {'X', 'Y', 'Z'}:
            raise ValueError("Invalid axis. Axis must be 'X', 'Y', or 'Z'.")
        self.send_gcode(f"G28 {axis}")

    def home_all(self):
        self.send_gcode(f"G28 X Y Z")
    
    def set_acceleration(self, acceleration, travel_acceleration):
        self.send_gcode(f"M204 P{acceleration} T{travel_acceleration}")

    def set_feedrate(self, feedrate):
        self.feedrate = feedrate
