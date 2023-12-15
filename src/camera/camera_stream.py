from flask import Flask, Response, send_file
import subprocess
import time

app = Flask(__name__)

def capture_image():
    filename = "/tmp/camera_image.jpg"
    subprocess.run(["libcamera-still", "-o", filename])
    return filename

@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
            # Capture an image
            image = capture_image()
            
            # Yield the image as a response
            with open(image, 'rb') as f:
                frame = f.read()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

            time.sleep(1)  # Adjust the delay as needed

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return """
    <html>
    <head>
    <title>Raspberry Pi - libcamera Stream</title>
    </head>
    <body>
    <h1>Raspberry Pi - libcamera Stream</h1>
    <img src="/video_feed">
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)