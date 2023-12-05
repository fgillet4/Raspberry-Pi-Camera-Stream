from flask import Flask, render_template, request, redirect, url_for
import camera_stream  # Assuming camera_stream.py is in the same directory
import database_manager  # Assuming database_manager.py is in the same directory
import json
from dotenv import load_dotenv
load_dotenv()


# Load the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Accessing configuration values
flask_config = config['flask']
camera_config = config['camera']
database_config = config['database']

app = Flask(__name__)

# Initialize the database manager
db_manager = database_manager.DatabaseManager()

@app.route('/')
def index():
    # Render the main page (index.html)
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Video streaming route. This uses the method from camera_stream.py
    return camera_stream.video_feed()

@app.route('/submit_reading', methods=['POST'])
def submit_reading():
    # Handle the form submission for manual pressure reading entry
    if request.method == 'POST':
        reading = request.form['pressureReading']
        timestamp = request.form['timestamp']  # You might want to handle timestamp differently

        # Write the reading to the database
        db_manager.write_pressure_reading(reading, timestamp)

        # Redirect back to the main page
        return redirect(url_for('index'))

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        db_manager.close()
