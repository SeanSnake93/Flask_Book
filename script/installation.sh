#!/usr/bin/env bash

cd /var/lib/jenkins/workspace/Flask_book
 
sudo apt update -y
 
sudo apt install python3 -y
 
sudo apt install python3-pip -y
 
sudo apt install python3-venv -y
 
python3 -m venv venv

. /var/lib/jenkins/workspace/Flask_book/venv/bin/activate

source ~/.bashrc

pip3 install -r requirements.txt

pytest --cov ./application --cov-report html

mv ./htmlcov/index.html ./application/templates/coverage.html

rm -rf htmlcov
 
gunicorn --bind=0.0.0.0:5000 app:app