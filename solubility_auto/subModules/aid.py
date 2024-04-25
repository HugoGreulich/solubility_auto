import configparser
import time

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

class help:
    def get_coords():
        coordinates = {}
        #letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        letters = ['A', 'B']
        x = A1_x
        for letter in letters:
            y = A1_y
            for i in range(1, 13):
                coordinates[f'{letter}{i}'] = (x, y)
                y -= 9
            x -= 9
        return coordinates
    
    def wait(seconds):
        time.sleep(seconds)