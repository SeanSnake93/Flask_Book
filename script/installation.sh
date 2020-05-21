#!/usr/bin/env bash
 
sudo apt update -y
 
sudo apt install python3 -y
 
sudo apt install python3-pip -y
 
sudo apt install python3-venv -y
 
python3 -m venv venv
 
source /var/lib/jenkins/workspace/Flask_Book/venv/bin/activate
 
pip3 install -r requirements.txt
 
cd /var/lib/jenkins/workspace/Flask_Book
 
source ~/.bashrc
 
gunicorn --bind=0.0.0.0:5000 app:app