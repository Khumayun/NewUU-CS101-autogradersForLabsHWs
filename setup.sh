#!/usr/bin/env bash

echo "Installing apt dependencies..."
apt-get install -y python3 python3-pip python3-dev

echo "Installing python3 dependencies..."
pip3 install -r /autograder/requirements.txt

echo "Installing Gradescope dependencies..."
cd /autograder/GradescopeBase-master
python3 setup.py install
cd ../
