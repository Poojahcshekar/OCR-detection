import cv2
import numpy as np
import pytesseract
import re
import matplotlib.pyplot as plt
#from skimage import morphology

cap = cv2.VideoCapture('din5 babau.wmv')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
font = cv2.FONT_HERSHEY_COMPLEX

i=1
str = ''
prev_str = ''
str_show = ''
output=open("Report1.txt",'w')
fixedfps=40
x=[]
y=[]
l=[]
h=[]
while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    kernel = np.ones((1, 1), np.uint8)
    hsv = cv2.dilate(hsv, kernel, iterations=1)
    hsv = cv2.erode(hsv, kernel, iterations=1)
    fps=cap.get(cv2.CAP_PROP_FPS)
    timestamp=cap.get(cv2.CAP_PROP_POS_MSEC)
    # define range of white color in HSV
    # change it according to your need !
    sensitivity = 7
    lower_white = np.array([0,0,255-sensitivity], dtype=np.uint8)
    upper_white = np.array([255,sensitivity,255], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower_white, upper_white)
    
    i=i + 1
    result = ''
    if i == 30:
        result = pytesseract.image_to_string(mask)
        
        
        



    
    
    cv2.imshow('frame',frame)
 
    if(fps<10):
       
        print('frame drop at')
        print(timestamp)
        output.write(format(fps)+'\n')
        output.write('frame drop at:')
        output.write(format(timestamp)+' msec'+'\n')
        output.write('number of frames lost:'+format(fixedfps-fps)+'\n')
        output.write('\n')
   
    x.append(timestamp)
    y.append(fps)
    plt.plot(x,y)
   

    plt.xlabel('timestamp')
    plt.ylabel('fps')

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
output.close()
cv2.destroyAllWindows()
