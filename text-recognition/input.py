from ocr import extract_text
import cv2

img = cv2.imread('AB_Crepes.jpeg')

def show_image(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)

def get_text(image):
    print(extract_text(image))

show_image(img)
get_text(img)