import cv2 as cv 
import numpy as np 

cap = cv.VideoCapture(0)

#load haarcascades 
face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')

#load image 
img = cv.imread('image/edward.jpg')

#open camera 
while True: 
    ret, frame = cap.read() 
    if not ret: 
        break 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #detect faces 
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x1, y1, w1, h1) in faces: 
        cv.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (218, 65, 103), 2)
        img_resized = cv.resize(img, (w1, h1), interpolation=cv.INTER_LINEAR)
        frame[y1:y1+h1, x1:x1+w1] = img_resized
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]
    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'): 
        break

#display image 
cap.release()
cv.destroyAllWindows()