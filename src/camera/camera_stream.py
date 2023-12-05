from flask import Flask, Response
import picamera
import threading
import io
import json

# Load the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Accessing configuration values
flask_config = config['flask']
camera_config = config['camera']
database_config = config['database']


# Initialize Flask application
app = Flask(__name__)

# Initialize camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24

# Create a buffer for camera image stream
stream = io.BytesIO()

# Function to continuously capture video frames and store them in the stream
def camera_stream():
    with camera:
        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')
            stream.seek(0)
            stream.truncate()

# Route for video streaming
@app.route('/video_feed')
def video_feed():
    return Response(camera_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Main route
@app.route('/')
def index():
    # return a static HTML page with the video feed
    return """
    <html>
    <head>
    <title>Raspberry Pi Camera Stream</title>
    </head>
    <body>
    <h1>Raspberry Pi Camera Stream</h1>
    <img src="/video_feed">
    </body>
    </html>
    """

if __name__ == '__main__':
    try:
        # Start the Flask web server
        app.run(host='0.0.0.0', port=5000, threaded=True)
    finally:
        camera.close()
