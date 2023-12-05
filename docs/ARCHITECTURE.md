# Project Architecture
This document outlines the architecture of the Raspberry Pi Pressure Gauge Monitoring System. The system is designed to capture and stream video from a Raspberry Pi camera, display the stream on a Flask-based web interface, and allow manual entry of pressure readings. Future enhancements will include machine learning for automatic pressure reading.

# Directory Structure
`src`: Contains the source code for the entire project.

`camera`: Code related to the Raspberry Pi camera and video streaming.
`camera_stream.py`: Handles the camera streaming functionality.
`web`: Code for the Flask web server and interface.
`app.py`: Main Flask application file.
`templates`: HTML templates for the web interface.
`index.html`: Main webpage template.
`static`: Static files like CSS and JavaScript.
`style.css`: CSS styles for the web interface.
`database`: Database interaction scripts.
`database_manager.py`: Manages database operations.
`ml_model`: (Future) Machine learning model for pressure reading.
`model.py`: Placeholder for machine learning model code.
`data`: Data used for model training.
`tests`: Contains unit tests and integration tests for the application.

- Example: test_camera.py
`docs`: Documentation files for the project.

`README.md`: Overview and setup instructions.
`CONTRIBUTING.md`: Guidelines for contributing to the project.
`ARCHITECTURE.md`: This architecture documentation.
`config`: Configuration files for the application.

`config.json`: Contains configurable parameters and settings.
`scripts`: Utility scripts for setup and maintenance.

- Example: install_dependencies.sh
`backups`: Backup directory for important data.

`.gitkeep`: Ensures the directory is tracked by Git.
# Key Components
- Flask Web Server: Serves the web interface and handles requests, including streaming video and processing form submissions for manual data entry.
- Raspberry Pi Camera: Captures and streams video of the pressure gauge.
- InfluxDB: Database used for storing pressure readings.
- Machine Learning Model: (Future development) Will be used for automatic detection and reading of pressure gauge values.
# Security Considerations
The system is designed to operate on a local network, with no external internet access to ensure security.
Manual data entry is validated to prevent SQL injection or other forms of malicious input.
# Future Enhancements
Integration of a machine learning model to automate the reading of pressure values from the camera feed.
Improved error handling and logging for robust operation.