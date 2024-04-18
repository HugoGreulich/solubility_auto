import sys
sys.path.append("../solubility_auto")

from solubility_auto.CarthesianRobot import CarthesianRobot
import configparser

config_path = r'C:\Users\Hugo Greulich Mayor\Documents\GitHub\solubility_auto\config\anycubic_kobra_neo_2.ini' # check pour plus simple

config = configparser.ConfigParser()
config.read(config_path)
port = config.get('DEFAULT', 'port')
baudrate = config.getint('DEFAULT', 'baudrate')
init_x = config.get('SETTINGS', 'init_x')
init_y = config.get('SETTINGS', 'init_y')
init_z = config.get('SETTINGS', 'init_z')

robot = CarthesianRobot()
robot.connect_serial(port, baudrate)
robot.set_acceleration(5000, 5000)
#robot.home_all()
#robot.move_absolute(None, None, 100)
#robot.move_absolute(init_x, init_y, init_z)
robot.move_relative(10,10,10)
robot.disconnect_serial()
