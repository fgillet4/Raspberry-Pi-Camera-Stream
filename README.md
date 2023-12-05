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

# Raspberry Pi Headless Setup Guide

After flashing the Raspberry Pi OS onto an SD card using tools like Etcher, follow these steps to set up your Pi for headless access (without a monitor).

## 1. Enable SSH Access

To enable SSH access:
- Create an empty file named `ssh` (with no file extension) and place it in the root directory of the boot partition.
- You may have to navigate to the bootfs partition (Ubuntu) 

## 2. Set Up WiFi (Optional)

Note:Make sure the wifi you are using is 2.4 GHz since the pi only supports 2.4 GHz

If you want your Raspberry Pi to connect to your WiFi network on boot:
1. Create a file named `wpa_supplicant.conf` in the root directory of the boot partition.
2. Add the following content, replacing with your actual WiFi details:
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="YOUR_WIFI_SSID"
psk="YOUR_WIFI_PASSWORD"
key_mgmt=WPA-PSK
}
```

Ensure to replace `YOUR_WIFI_SSID` and `YOUR_WIFI_PASSWORD` with your WiFi credentials. If you're not in the US, adjust the `country` field accordingly.

## 3. Safely Eject the SD Card

- Ensure you safely eject the SD card from your computer.

## 4. Boot Your Raspberry Pi

- Insert the SD card into the Raspberry Pi and power it on.
- After it's booted up, you can access your Raspberry Pi via SSH from another computer on the same network using:

ssh pi@raspberrypi.local

The default password is `raspberry`.

## 5. Setting a Secure Password

For enhanced security, it's recommended to change the default password to something unique. You can generate a secure password hash using:
```bash
echo 'your_password' | openssl passwd -6 -stdin
```
This command will provide you with a hashed version of your password. Use this hash when setting up password authentication in relevant configuration files.




# How to Detach the Flask Server from the SSH Session

This README guides you on how to manage and monitor the Humidity Control Arduino service running on a Raspberry Pi. You can both use the `screen` method to run it interactively and the systemd service to run it as a background process.

## Using `screen`:

### **Installing `screen`:**
```bash
sudo apt-get update
sudo apt-get install screen
```

### **Starting the Script with `screen`:**

1. SSH into your Raspberry Pi:
    ```bash
    ssh raspberrypi@raspberrypi.local
    ```

2. Start a new `screen` session named "arduino":
    ```bash
    screen -S arduino
    ```

3. Run the script:
    ```bash
    sudo python3 web_server.py
    ```

4. Detach from the `screen` session with `CTRL` + `A` followed by `CTRL` + `D`.

### **Re-attaching to the `screen`:**

If you want to see the live output or interact with the running script:
```bash
screen -r arduino
```

## Use systemd to restart the Web Server upon reboot of the Pi:

`humidity-control.service` should already be in the directory

### **Starting the Service:**
```bash
sudo systemctl start humidity-control.service
```

### **Stopping the Service:**
```bash
sudo systemctl stop humidity-control.service
```
### **Restarting the Service:**
```bash
sudo systemctl restart humidity-control.service
```
### **Status of the Service:**
```bash
sudo systemctl status humidity-control.service
```

# Setting Up Custom Hostname on Raspberry Pi

## **1. Setting up Raspberry Pi**

- Start with a fresh install of Raspberry Pi OS (formerly Raspbian) on your Raspberry Pi.

## **2. Boot up and connect**

- Once you've booted up, connect to your Raspberry Pi either directly (using a monitor, keyboard, etc.) or SSH into it using its default hostname:

  ```bash
  ssh pi@raspberrypi.local
  ```

  > Default password is usually `raspberry`.

## **3. Change the hostname**

- Once connected, edit the `hostname` file:

  ```bash
  sudo nano /etc/hostname
  ```

  - Replace the default name `raspberrypi` with your desired name. For this guide, we'll use `krypgrund` which means "crawlspace" in Swedish, you can use any name you like.

- Next, update the `hosts` file:

  ```bash
  sudo nano /etc/hosts
  ```

  - Find the line that reads `127.0.1.1 raspberrypi` and change `raspberrypi` to `krypgrund`.

## **4. Reboot the Raspberry Pi**

- For the changes to take effect, reboot the Raspberry Pi:

  ```bash
  sudo reboot
  ```

## **5. Connect using the new hostname**

- After the reboot, you can now SSH into your Raspberry Pi using the new hostname:

  ```bash
  ssh pi@krypgrund.local
  ```

  > Remember to use the password you've set previously.

## **6. All done!**

- Your Raspberry Pi is now accessible via the new hostname `krypgrund.local`.

# Changing Default SSH Username on Raspberry Pi

## **1. Log into your Raspberry Pi**

- Start by SSHing into your Raspberry Pi using the default credentials:

  ```bash
  ssh pi@krypgrund.local
  ```

  > Default password is usually `raspberry`.

## **2. Create a new user**

- Once logged in, add a new user called `krypgrund`:

  ```bash
  sudo adduser krypgrund
  ```

  - Follow the prompts to set a password and provide any additional information (or just press enter for defaults).

## **3. Grant the new user sudo privileges**

- To ensure the new user can perform administrative tasks, add them to the `sudo` group:

  ```bash
  sudo usermod -aG sudo krypgrund
  ```

## **4. Test the new user**

- Before making any further changes, SSH into the Raspberry Pi using the new user to ensure everything is working:

  ```bash
  ssh krypgrund@krypgrund.local
  ```

  > Enter the password you set for `krypgrund` when prompted.

## **5. Disable the default `pi` user**

- For security reasons, it's a good idea to disable the default `pi` user once you're certain your new user works:

  ```bash
  sudo passwd -l pi
  ```

  This locks the `pi` account.

## **6. All done!**

- You've successfully changed the default SSH user. Now you can log in with:

  ```bash
  ssh krypgrund@krypgrund.local
  ```
# Raspberry Pi DDNS Client Setup Instructions

Follow these steps to set up Dynamic DNS on your Raspberry Pi, which will keep your network accessible through a fixed hostname despite a changing public IP address.

## Prerequisites

* A Raspberry Pi running Raspberry Pi OS
* An internet connection
* A DDNS account (e.g., No-IP)

## Installation and Configuration

### 1. Update Your System

Ensure your Raspberry Pi is up to date:

```shell
sudo apt update
sudo apt upgrade
```

## *2. Install DDclient
Install the `ddclient` package:

```shell
sudo apt install ddclient
```

## *3. Configure DDclient
Install the `ddclient` package:

```shell
sudo nano /etc/ddclient.conf
```

Add your DDNS service configuration:

```
protocol=dyndns2
use=web, web=checkip.dyndns.com/, web-skip=/"IP Address"/
server=dynupdate.no-ip.com
login=your_noip_login
password=/your_noip_password/
your_noip_hostname
```
Make sure to replace your_noip_login, /your_noip_password/, and your_noip_hostname with your actual No-IP credentials and hostname.

## *4. Enable and Start the DDclient Service
Enable `ddclient` to start on boot:

```shell
sudo systemctl enable ddclient
```
Start the `ddclient` service:


```shell
sudo systemctl start ddclient
```

## *5. Testing the Configuration

Force an immediate update with:


```shell
sudo ddclient -force
```
Start the `ddclient` service:

## *6. Check for Errors

Review the `ddclient` logs if needed:

```shell
grep ddclient /var/log/syslog
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Raspberry Pi Foundation](https://www.raspberrypi.org/)
- [InfluxDB](https://www.influxdata.com/)

