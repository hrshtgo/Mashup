# Mashup Web Service

## Roll No: 102003644

## Description
This web service generates a unique blend of videos of your preferred singer. Simply enter the singer name, the number of videos, the audio duration, and the email ID where you want to send the zipped mashup file. Note that the app may take some time to execute as it requires downloading multiple audio files from the internet.

## Requirements
* Run the following commands in terminal:
```
pip install waitress
pip install pytube
pip install pydub
pip install flask
```
* Install ffmpeg via https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/.

## Using the web app
Navigate to the folder where you have downloaded the above files and open [run.py].

Enter the required entries in the webpage that opens and hit submit. The given email id should recieve a zip file containing the desired audio file.
Webpage can be changed by editing the php code in templates named [index.html].

The webapp can be hosted online on a platform that allows the following:
* SMTP transfer via port 465.
* Downloading and storing files from YouTube.
