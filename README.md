# Raspberry Pi Camera Streaming Project

This repository contains the code and instructions to set up a Raspberry Pi with a camera module for streaming video over a local network. Additionally, it includes the steps to log pressure gauge readings to an InfluxDB database. The project also discusses future development plans for machine learning integration.

## Prerequisites

Before starting, ensure you have the following:

- Raspberry Pi (any model with a camera module)
- microSD card (8GB or larger)
- Power supply for the Raspberry Pi
- USB keyboard and mouse
- HDMI display and cable (for initial setup)
- Internet access
- Ubuntu computer (for writing the Raspberry Pi OS image to the microSD card)

## Setting Up the Raspberry Pi

1. Download the latest Raspberry Pi OS image:
   ```bash
   wget https://downloads.raspberrypi.org/raspios_lite_armhf_latest
   ```

2. Write the OS image to the microSD card (replace `/dev/sdX` with your microSD card's device identifier):
    ```bash
    sudo dd bs=4M if=raspios_lite_armhf_latest of=/dev/sdX conv=fsync
    ```
3. Insert the microSD card into your Raspberry Pi and power it on.

4. Follow the on-screen instructions to set up the Raspberry Pi, including configuring Wi-Fi, localization, and password.

## Installing the Camera Module

1. Connect the Raspberry Pi Camera Module to the Pi's CSI port.

2. Enable the camera module using `raspi-config`:
    ```bash
    sudo raspi-config
    ```
3. Navigate to "Interfacing Options" > "Camera" and enable the camera.

## Setting Up the Flask Server

1. Install Flask on your Raspberry Pi:
```bash
pip install flask
```

2. Clone this repository:
```bash
git clone https://github.com/fgillet4/Raspberry-Pi-Camera-Stream
```

3. Navigate to the project directory:
```bash
cd Raspberry-Pi-Camera-Stream
```


4. Start the Flask server:
```bash
python app.py
```


5. Access the video stream on a web browser using the Raspberry Pi's IP address and port 5000 (e.g., `http://<raspberry_pi_ip>:5000`).

## Logging Pressure Gauge Readings

1. Set up InfluxDB on your Raspberry Pi and create a database for the project.

2. Install the InfluxDB Python client:
```bash
pip install influxdb
```


3. Modify the Flask application to log pressure gauge readings and save them to the InfluxDB database.

4. Add a web interface to manually input pressure readings and log them to the database.

## Future Development (Machine Learning)

- Train a machine learning model to detect and analyze pressure gauge readings.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Raspberry Pi Foundation](https://www.raspberrypi.org/)
- [InfluxDB](https://www.influxdata.com/)

