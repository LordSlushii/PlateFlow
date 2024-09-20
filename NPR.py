import cv2
import pytesseract
import numpy as np
from PIL import Image
import csv
import os 


char_valid = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789"

def NPR():

    final_text =""
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Ask the user to input the directory of the image file
    file_path = input("Enter the directory of the image file: ")   
    img = cv2.imread(file_path)    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Apply dilation to the thresholded image
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    # Convert the dilated image to a PIL image
    pil_img = cv2.cvtColor(dilated, cv2.COLOR_GRAY2RGB)
    pil_img = Image.fromarray(pil_img)
    # Configure pytesseract to use English language and OCR engine
    custom_config = r'--oem 3 --psm 6'
    # Load the image using pytesseract
    text = pytesseract.image_to_string(pil_img, config=custom_config)
    # Print the extracted text
    
    for i in text :
        if i in char_valid:
            final_text += i
    print("Number Plate:", final_text)
        
NPR()
