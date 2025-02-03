from flask import Flask, render_template, Response, request 
import cv2 as cv 
from filters import add_filter 

app = Flask(__name__)

@app.route('/')
def main_page(): 
    return render_template('index.html')

@app.route('/process')
def process(): 
    character = request.args.get('char')
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
            frame = add_filter(frame, character)
            _, buffer = cv.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    return Response(video_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cam')
def cam(): 
    character = request.args.get('character')
    name = request.args.get('name')
    return render_template('cam.html', character = character, name = name)

if __name__ == '__main__':
    app.run(debug=True)