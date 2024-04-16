#!/bin/sh

# Change to the app directory
cd /home/app

# If there is not a virtual environment for linux, remove the existing one
# This is to ensure that the virtual environment is created for the correct OS (Linux)
if [ ! -d "functions/venv/bin" ]; then
    rm -rf functions/venv
fi

# Create a virtual environment
if [ ! -d "functions/venv" ]; then
    python -m venv functions/venv
fi
source functions/venv/bin/activate
pip install -r functions/requirements.txt

# Install npm packages
npm install

# Login to firebase
npx firebase login

# Start firebase emulator
npx firebase emulators:start --only functions