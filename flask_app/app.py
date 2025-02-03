from flask import Flask, render_template, Response 
import cv2 as cv 
from filters import add_filter 

app = Flask(__name__)

def video_frame(): 
    cam = cv.VideoCapture(0)
    cam.set(cv.CAP_PROP_FRAME_WIDTH, 800)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, 600)
    while True:
        ret, frame = cam.read()
        if not ret: 
            print("Camera failed")
            break    
        rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        _, buffer = cv.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n') 

@app.route('/')
def main_page(): 
    return render_template('index.html')

@app.route('/video')
def video(): 
    return Response(video_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/process')
def process(): 
    def video_frames():
        cam = cv.VideoCapture(0)
        cam.set(cv.CAP_PROP_FRAME_WIDTH, 800)
        cam.set(cv.CAP_PROP_FRAME_HEIGHT, 600)
        while True:
            ret, frame = cam.read()
            if not ret: 
                print("Camera failed")
                break    
            rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame = add_filter(frame, 'flask_app/filters/edward.jpg')
            _, buffer = cv.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    return Response(video_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cam')
def cam(): 
    return render_template('cam.html')

if __name__ == '__main__':
    app.run(debug=True)