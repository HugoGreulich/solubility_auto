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
#robot.home_all()
#robot.move_to_rest()

robot.move_absolute(103,175,90)
#robot.move_absolute(A1_x, A1_y, pos_low)
#robot.wait(15)
#robot.move_up()

robot.disconnect_serial()