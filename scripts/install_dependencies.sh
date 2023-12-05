#!/bin/bash

# This script installs the necessary dependencies for the Raspberry Pi Pressure Gauge Monitoring System.

echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

echo "Installing Python3 and pip..."
sudo apt-get install -y python3 python3-pip

echo "Installing Python packages required by the project..."
pip3 install Flask picamera influxdb-client

echo "Installing InfluxDB (if required by your project)..."
# Add commands to install InfluxDB here, if it's not already installed.
# This might vary based on your InfluxDB version and setup requirements.

echo "Installation complete. All necessary dependencies are installed."
