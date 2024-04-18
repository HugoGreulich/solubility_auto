import serial
import time

class CartesianRobot:
    def __init__(self):
        self.serial = None
        self.feedrate = 1500  # Set default feedrate

    def connect_serial(self, port, baudrate):
        """
        Establishes a serial connection using specified settings.
        """
        self.serial = serial.Serial(port, baudrate, timeout=1)
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

    def move_relative(self, x=None, y=None, z=None):
        self.send_gcode("G91")  # Set to relative positioning
        self.move_axis(x, y, z)

    def move_absolute(self, x=None, y=None, z=None):
        self.send_gcode("G90")  # Set to absolute positioning
        self.move_axis(x, y, z)

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

    def set_acceleration(self, acceleration, travel_acceleration):
        self.send_gcode(f"M204 P{acceleration} T{travel_acceleration}")

    def set_feedrate(self, feedrate):
        self.feedrate = feedrate
