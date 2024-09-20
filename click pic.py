import cv2 
import time
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