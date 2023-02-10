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

## Using the Web App
* Navigate to the folder where you have downloaded the above files and open [run.py].

* Hit submit after filling the required entries in the webpage that opens and the input email id will receive a zip file containing an audio file which can be renamed to any audio file extension format [for eg: .mp3].

* The appearance of the webapp can be changed by editing the HTML file named [index.html] in the templates folder.

* The webapp can be hosted online on a platform that allows the following:
** SMTP via port 465.
** Downloading and storing files from YouTube.

As of now there were no free online platforms that satisfy both the conditions and therefore I have provided the link to this repository.
