import cv2
import pytesseract
import numpy as np
from PIL import Image
import csv
import os

char_valid = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
L_ST = ['TN','KL','SK','TS','TR','DL','KA','AP','AR','MH','GA','MP','UP','GJ','RJ','HR','PB','JK','JH','WB','AS','CG','HP','ML','MN','MZ','OD','BR','NL']
str_st = "TKSDAMGRGCHOB"
def NPR(img_name):
    directory_image = r'C:\Users\krish\Downloads'
    final_directory_image = os.path.join(directory_image, img_name)
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
    
    img = cv2.imread(final_directory_image)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    
    pil_img = cv2.cvtColor(dilated, cv2.COLOR_GRAY2RGB)
    pil_img = Image.fromarray(pil_img)
  
    custom_config = r'--oem 3 --psm 6'
    
    text = pytesseract.image_to_string(pil_img, config=custom_config)
    
    final_text = ""
    for i in text :
        if i in char_valid:
            final_text += i
    temp_str =""
    
        
            
    print("Number Plate:", final_text)

def dikpik():
    global img_name 
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("TEST")
    img_counter = 0
    while True:
        ret,frame = cam.read()
        if not ret:
            break
        
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            break
        elif k%256 == 32:
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name,frame)
            img_counter += 1
            
    cam.release()
    cv2.destroyAllWindows()
    
    return img_name
    
img_name = dikpik()
NPR(img_name)


# Path to the CSV file
csv_file = 'orders.csv'

# Function to add or update an order in the CSV
def update_order(license_plate, current_order):
    # Check if file exists, if not, initialize it
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["License Plate", "Current Order", "Previous Orders"])  # Write header if file is new
    
    # Load existing data
    rows = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Check if license plate exists
    license_found = False
    for row in rows:
        if row[0] == license_plate:
            # If found, update current and previous orders
            row[2] = f"{row[2]}; {row[1]}" if row[2] else row[1]  # Move current order to previous orders
            row[1] = current_order           # Update with new current order
            license_found = True
            break
    
    # If not found, add a new entry
    if not license_found:
        rows.append([license_plate, current_order, ""])

    # Write updated data back to the CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Function to read the data from the CSV
def read_orders():
    if not os.path.exists(csv_file):
        print("No orders found.")
        return
    
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"License Plate: {row[0]}, Current Order: {row[1]}, Previous Orders: {row[2]}")
read_orders()
update_order()