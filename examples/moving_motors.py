import sys
sys.path.append("../solubility_auto")

from solubility_auto.CarthesianRobot import CarthesianRobot
import configparser
import time

config_path = r'C:\Users\Hugo Greulich Mayor\Documents\GitHub\solubility_auto\config\anycubic_kobra_neo_2.ini'

config = configparser.ConfigParser()
config.read(config_path)
port = config.get('DEFAULT', 'port')
baudrate = config.getint('DEFAULT', 'baudrate')

robot = CarthesianRobot()
robot.connect_serial(port, baudrate)
robot.move_to_rest()

robot.disconnect_serial()