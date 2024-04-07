# Mood Room Camera
Mood Room is a service that allows users to automatically control their environment in response to their current mood. Users setup a Mood Room Camera in a convenient location in their room, configure their environment settings and hardware in the Mood Room GUI, and Mood Room's software takes it from there.  
  
Mood Room Camera is the sensing system of this service, which is built on Raspberry Pi and leverages OpenCV and Amazon Rekognition to detect the user's emotions.  

## Prerequisites
Setup the Raspberry Pi and Camera Module, and verify that the camera works with `rpicam-hello`. This system is tested on a Raspberry Pi 4 Model B 8GB running Raspberry Pi OS (bookworm), with a Camera Module Rev 1.3.  
Install and configure [AWS CLI](https://aws.amazon.com/cli/) for use with [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html)

## Installation
Execute the following in the terminal:  
`git clone https://github.com/starphys/MoodRoomCamera.git`  
`cd MoodRoomCamera`  
If desired, create and activate a virtual environment for this project. Pass the flag `--system-site-packages` when creating the environment to ensure access to picamera2. Execute the following in the terminal:  
`pip install -r requirements.txt`  

## Usage
From the same directory, execute the following in the terminal:  
`python main.py`  
Your Mood Room Camera is now running! It will send an image to Amazon Rekognition once every two minutes, and only if OpenCV detected a face currently in frame. If no faces are detect, the system will try again every 7 seconds.