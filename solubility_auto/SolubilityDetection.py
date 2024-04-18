import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

class SolubilityDetection:
    def color_gray(img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return gray
    
    def color_rgb(img):
        rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return rgb