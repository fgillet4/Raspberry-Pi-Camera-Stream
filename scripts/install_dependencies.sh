#!/bin/bash

# This script installs the necessary dependencies for the Raspberry Pi Pressure Gauge Monitoring System.

echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

echo "Installing Python3 and pip..."
sudo apt-get install -y python3 python3-pip python3-venv

echo "Setting up a Python virtual environment for the project..."
python3 -m venv ~/pi-venv

echo "Activating the virtual environment..."
source ~/pi-venv/bin/activate

echo "Installing Python packages required by the project within the virtual environment..."
pip install Flask picamera influxdb-client

echo "Deactivating the virtual environment..."
deactivate

echo "Installation complete. All necessary Python dependencies are installed in the virtual environment."

echo "Installing InfluxDB (if required by your project)..."
# Add commands to install InfluxDB here, if it's not already installed.
# This might vary based on your InfluxDB version and setup requirements.
