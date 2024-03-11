#!/usr/bin/env bash

echo "Installing apt dependencies..."
apt-get install -y python3 python3-pip python3-dev

echo "Installing python3 dependencies..."
pip3 install -r /autograder/source/requirements.txt

echo "Installing Gradescope dependencies..."
cd /autograder/source/GradescopeBase-master
python3 setup.py install
cd ../
