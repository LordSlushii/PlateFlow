import cv2
import pytesseract
import numpy as np
from PIL import Image
import csv
import os
from customtkinter import *
from datetime import date
from datetime import datetime
from datetime import time 
##The scanning of numberplate 
char_valid = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
L_ST = ['TN','KL','SK','TS','TR','DL','KA','AP','AR','MH','GA','MP','UP','GJ','RJ','HR','PB','JK','JH','WB','AS','CG','HP','ML','MN','MZ','OD','BR','NL']
str_st = "TKSDAMGRGCHOB"
final_text =""
def NPR(img_name):
    global final_text 
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
    return final_text
    

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
    NPR(img_name)
    return img_name
    

def Lisc_Plate():
    NPR(dikpik())


##---------------------------------------------------------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------------------------------------------------------


# CSV File / our data 
csv_file = 'orders.csv'


cr_date = date.today()
cr_time = datetime.now().strftime("%H:%M:%S")
# Function to add or update an order in the CSV
def update_order(final_text, current_order_L):
    previous_order = []
    # Check if file exists, if not, initialize it
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["License Plate", "Current Order", "Previous Orders","Time","Date","Time"])  # Write header if file is new
    if os.path.exists(csv_file):
        with open(csv_file, mode='w+', newline='') as file:
            cswriter = csv.writer(file)
            csreader = csv.reader(file)
            for i in (csreader):
                if i[0] == final_text:
                    if i [2] == None:
                     previous_order = []
                     previous_order.append(current_order)
                     cswriter.writerow([final_text, current_order, previous_order_L,cr_date,cr_time])
                    else:
                        previous_order = i[2]
                        previous_order.append(current_order)
                        cswriter.writerow([final_text, current_order, previous_order_L,cr_date,cr_time])

    
            
    
    # Load existing data
    rows = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Check if license plate exists
    license_found = False
    for row in rows:
        if row[0] == Lisc_Plate:
            # If found, update current and previous orders
            row[2] = f"{row[2]}; {row[1]}" if row[2] else row[1]  # Move current order to previous orders
            row[1] = current_order           # Update with new current order
            license_found = True
            break
    
    # If not found, add a new entry
    if not license_found:
        rows.append([final_text, current_order, ""])

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



home = CTk()
home.geometry("400x200")
def close():
    home.destroy()
#Decoration

title = CTkLabel(master=home, text = "PlateFlow", font = ("Coolvetica", 30), text_color="#FF6B00")
title.place(relx = 0.5, rely =0.12, anchor = "center")

subtitle = CTkLabel(master= home, text= "Your Drive-Thru Experience Made Seemless!", font = ("Coolvetica", 15), text_color="#FFFFFF")
subtitle.place(relx = 0.5, rely = 0.25, anchor = "center")



#Buttons

register = CTkButton(master=home, text= "Register ", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130 ,command =Lisc_Plate )
register.place(relx = 0.32, rely = 0.55, anchor = "center")

history=  CTkButton(master=home, text= "History", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130)
history.place(relx = 0.68, rely = 0.55, anchor = "center")

close = CTkButton(master=home, text= "Close", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130, command= close)
close.place(relx = 0.5, rely = 0.85, anchor = "center")

home.mainloop()





while True :
    
    ch_1 = int(input('''What Function would you like to do :
1) Add Order
2) View Order
3) Exit
'''))





    if ch_1 == 1:
        no_items = int(input("How many items would you liek to order :"))
        current_order_L = []
        for i in range(no_items):
            current_order = input("Enter your items :")
            current_order_L.append(current_order)
        update_order(Lisc_Plate,current_order_L)
    if ch_1 == 2:
        read_orders()
    if ch_1 == 3:
        break 
        
        
    
