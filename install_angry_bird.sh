#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
sudo apt update
sudo apt upgrade
sudo apt-get install python3-pip
sudo apt install redis-server
sudo systemd enable redis
sudo systemd start redis
sudo apt install cockpit
curl https://download.argon40.com/argon1.sh | bash
mkdir -p ~/projects/bots/
cd ~/projects/bots/
sudo apt install git
git clone https://github.com/Snoobdog10x/angry-bird.git
cd ~/projects/bots/angry-bird
sudo cp angry-bird.service /etc/systemd/system
sudo systemctl enable angry-bird.service
sudo systemctl start angry-bird.service