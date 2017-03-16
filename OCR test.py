import cv2
import numpy as np
import matplotlib
img = cv2.imread('C:\Users\Deji Salau\PycharmProjects\PlateRecognition\10.tif')
from PIL import Image as img
SetVariable("tessedit_char_whitelist", "BCDFGHJKLMNPQRSTVWXYZ0123456789-")
SetVariable("language_model_penalty_non_freq_dict_word", "1")
SetVariable("language_model_penalty_non_dict_word ", "1")
SetVariable("load_system_dawg", "0")
import Image
from PIL import Image
import pytesseract
print(pytesseract.image_to_string(Image.open('1.jpg')))
print(pytesseract.image_to_string(Image.open('img'), lang='fra'))
