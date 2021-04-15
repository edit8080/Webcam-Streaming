from flask import Flask, render_template, Response
import cv2


app = Flask(__name__)
camera = cv2.VideoCapture(1)


# 카메라에서 Frame 받아오기
def gen():
    while True:
        success, frame = camera.read()
        frame = cv2.flip(frame, 1)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


# 비디오 스트리밍
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
