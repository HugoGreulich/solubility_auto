import sys
sys.path.append("../solubility_auto")

from solubility_auto.CarthesianRobot import CarthesianRobot
from solubility_auto.subModules.aid import help
import configparser

config_path = r'C:\Users\Hugo Greulich Mayor\Documents\GitHub\solubility_auto\config\anycubic_kobra_neo_2.ini' # check pour plus simple

config = configparser.ConfigParser()
config.read(config_path)
port = config.get('DEFAULT', 'port')
baudrate = config.getint('DEFAULT', 'baudrate')
A1_x = config.get('SETTINGS', 'A1_x')
A1_y = config.get('SETTINGS', 'A1_y')
pos_low = config.get('SETTINGS', 'pos_low')
pos_high = config.get('SETTINGS', 'pos_high')
columns = config.getint('SETTINGS', 'columns')
rows = config.getint('SETTINGS', 'rows')
cam_zone1_x = config.getint('SETTINGS', 'cam_zone1_x')
cam_zone1_y = config.getint('SETTINGS', 'cam_zone1_y')

robot = CarthesianRobot()
robot.connect_serial(port, baudrate)
robot.set_acceleration(5000, 5000)
robot.home_all()

#coords = help.get_coords()
#for coord in coords:
#    robot.move_up()
#    robot.move_absolute(coords[coord][0], coords[coord][1], None)
#    robot.move_down()
#robot.move_to_rest()

#robot.move_up()
#robot.move_absolute(A1_x, A1_y, pos_high)
#robot.move_down()

#robot.move_absolute(A1_x, A1_y, pos_high)
#robot.move_down()
#for row_pair in range(rows/2):
#    column = 1
#    while column < columns:
#        robot.move_increase_nbr()
#        column += 1
#    robot.move_increase_let()
#    while column > 1:
#        robot.move_decrease_nbr()
#        column -= 1
#    robot.move_increase_let()

#robot.move_up()
#robot.move_absolute(cam_zone1_x, cam_zone1_y, None)

robot.disconnect_serial()
