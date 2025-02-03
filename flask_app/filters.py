import cv2 as cv 

def add_filter(frame, imgpath):
    face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
    img = cv.imread(imgpath)
    if img is None: 
        print("Image not found!!!!!!!")
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x1, y1, w1, h1) in faces: 
        cv.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), 2)
        img_resized = cv.resize(img, (w1, h1), interpolation=cv.INTER_LINEAR)
        frame[y1:y1+h1, x1:x1+w1] = img_resized
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]

    return frame