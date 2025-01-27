import cv2 as cv 

#load image 
img = cv.imread('image/stock1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#load haarcascades 
face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

#detect faces and eyes 
faces = face_cascade.detectMultiScale(gray, 1.3, 4)

for (x1, y1, w1, h1) in faces: 
    cv.rectangle(img, (x1, y1), (x1+w1, y1+h1), (218, 65, 103), 2)
    roi_gray = gray[y1:y1+h1, x1:x1+w1]
    roi_color = img[y1:y1+h1, x1:x1+w1]

eyes = eye_cascade.detectMultiScale(roi_gray)
for (x2, y2, w2, h2) in eyes: 
    cv.rectangle(roi_color, (x2, y2), (x2+w2, y2+h2), (99, 163, 117), 2)

#display image 
cv.imshow('image', img)

cv.waitKey(0)  
cv.destroyAllWindows()