import cv2 as cv 

cap = cv.VideoCapture(0)

#load haarcascades 
face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

#open camera 
while True: 
    ret, frame = cap.read() 
    if not ret: 
        break 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #detect faces and eyes 
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x1, y1, w1, h1) in faces: 
        cv.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (218, 65, 103), 2)
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (x2, y2, w2, h2) in eyes: 
            cv.rectangle(roi_color, (x2, y2), (x2+w2, y2+h2), (99, 163, 117), 2)

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'): 
        break

#display image 
cap.release()
cv.destroyAllWindows()