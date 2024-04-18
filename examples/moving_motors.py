from cartesian_robot.CarthesianRobot import CarthesianRobot
import configparser

config_path = 'anycubic_kobra_neo_2.ini'

config = configparser.ConfigParser()
config.read(config_path)
port = config.get('DEFAULT', 'port')
baudrate = config.getint('DEFAULT', 'baudrate')

robot = CarthesianRobot()
robot.connect(port, baudrate)
robot.move_axis('Y', -10, 3000)
robot.close_connection()