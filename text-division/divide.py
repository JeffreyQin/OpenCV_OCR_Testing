import easyocr
import cv2
import numpy as np
import os

path = "AB_Crepes.jpeg"
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

reader = easyocr.Reader(['en'])
text_data = reader.readtext(img)
print(text_data)