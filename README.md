# Mashup Web Service
Working Demonstration: https://youtu.be/n9eDh-yUaqQ

## Description
The web service generates a unique blend of videos of your preferred singer. Enter the singer's name, the number of videos, the audio duration, and the email ID where you want to send the zipped mashup file. Note that the app may take some time to execute as it requires downloading multiple audio files from the internet.

## Requirements
* Run the following commands in the terminal.
```
pip install waitress
pip install pytube
pip install pydub
pip install flask
```
* Install ffmpeg via https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/.

## Using the Web App
* Download [run.py] and open with python.

* Hit submit after filling in the required entries on the webpage that opens. 

* The input email id should receive a zip file containing an audio file that can be renamed to any audio file extension format [e.g., mashup.mp3]. 
  (Be sure to check the spam folder.)

The webapp can be hosted online on a platform that allows the following:
* SMTP via port 465.
* Downloading and storing files from YouTube.

As of now, there are no free online platforms that satisfy both conditions, so I have provided the link to this repository.
