import sys
sys.path.append("../solubility_auto")

from solubility_auto.CarthesianRobot import CarthesianRobot
import configparser

config_path = '.\config\anycubic_kobra_neo_2.ini'

config = configparser.ConfigParser()
config.read(config_path)
port = config.get('DEFAULT', 'port')
baudrate = config.getint('DEFAULT', 'baudrate')

robot = CarthesianRobot()
robot.connect_serial(port, baudrate)
robot.move_axis('Y', -10, 3000)
robot.disconnect_serial()