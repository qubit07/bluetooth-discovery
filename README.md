# Bluetooth Discovery

Build on Python 3.8.5 with PyBluez.

# Usage on Raspberry Pi

Require: Ubuntu Server 20.04 64Bit
Libaries: bluetooth, docker, docker-compose

Install:   
sudo apt install bluez

curl -fsSL https://get.docker.com -o get-docker.sh   
sudo sh get-docker.sh   
sudo usermod -aG docker ubuntu   

sudo apt install docker-compose   

Run:   
docker-compose up -d



