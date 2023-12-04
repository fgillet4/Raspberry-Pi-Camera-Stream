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

# Adding SSH Key to GitHub and Setting it for a Remote Repository

This guide will walk you through the process of adding an SSH key to your GitHub account and configuring it to work with a remote repository. SSH keys provide secure authentication for your Git operations.

## Step 1: Generate SSH Key

1. Open your terminal on your new computer.

2. Generate a new SSH key pair by running the following command:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Replace `"your_email@example.com"` with the email address associated with your GitHub account.

3. Press Enter to accept the default file location (`~/.ssh/id_rsa`) and create a passphrase (or leave it empty for no passphrase).

## Step 2: Add SSH Key to SSH Agent

1. Start the SSH agent by running:

```bash
eval "$(ssh-agent -s)"
```

2. Add your SSH private key to the SSH agent:

```bash
ssh-add ~/.ssh/id_rsa
```

## Step 3: Copy the SSH Public Key

1. To copy your SSH public key to the clipboard, use the following command:

```bash
cat ~/.ssh/id_rsa.pub | xclip -selection clipboard  # On Linux
```

Replace `xclip` with the appropriate clipboard tool for your operating system (e.g., `pbcopy` on macOS).

## Step 4: Add SSH Key to GitHub

1. Visit your GitHub account settings at [https://github.com/settings/profile](https://github.com/settings/profile).

2. In the left sidebar, click on "SSH and GPG keys."

3. Click the "New SSH key" button.

4. In the "Title" field, provide a descriptive title for the key (e.g., "New Computer SSH Key").

5. In the "Key" field, paste the SSH public key you copied in Step 3.

6. Click the "Add SSH key" button.

## Step 5: Configure Remote Repository

1. Open a terminal and navigate to your local Git repository's directory:

```bash
cd /path/to/your/repo
```

2. Check the current remote URL for your repository:

```bash
git remote -v
```

If it's using HTTPS, update it to use SSH. Replace `<username>` and `<repository>` with your GitHub username and repository name:

```bash
git remote set-url origin git@github.com:<username>/<repository>.git
```

## Step 6: Verify SSH Authentication

1. To verify that SSH authentication is set up correctly, run the following command:

```bash
ssh -T git@github.com
```

You should see a message like "Hi username! You've successfully authenticated..." if the connection is successful.

## Step 7: Push and Pull

1. You can now push and pull changes from your remote GitHub repository without being asked for your username and password:

```bash
git push origin <branch>
git pull origin <branch>
```

---

That's it! You've successfully added an SSH key to your GitHub account and configured it to work with a remote repository on your new computer. Your Git operations will now use SSH for secure authentication.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Raspberry Pi Foundation](https://www.raspberrypi.org/)
- [InfluxDB](https://www.influxdata.com/)

