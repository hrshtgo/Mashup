import os
import re
import smtplib
import urllib.request
from waitress import serve
from pytube import YouTube
from email import encoders
from zipfile import ZipFile
from pydub import AudioSegment
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, render_template
app=Flask(__name__) 
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        f=AudioSegment.empty()
        for i in range(int(request.form['number_of_videos'])):
            f+=AudioSegment.from_file(YouTube('https://www.youtube.com/watch?v='+re.findall(r'watch\?v=(\S{11})',urllib.request.urlopen('https://www.youtube.com/results?search_query='+str(request.form['singer_name'].replace(' ', '+'))).read().decode())[i]).streams.filter(only_audio=True).first().download(filename=str(i)))[:int(request.form['audio_duration'])* 1000]
            os.remove(str(i))
        f.export('mashup')
        with ZipFile('mashup.zip','w') as zip:
            zip.write('mashup')
        os.remove('mashup')
        m=MIMEMultipart()
        with open('mashup.zip',"rb") as attachment:
            part=MIMEBase("application","octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",f"attachment;filename={'mashup.zip'}",)
        m.attach(part)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login('mashupwebservice@gmail.com','vohhegrtknjctdyp')
            server.sendmail('mashupwebservice@gmail.com',request.form['email'],m.as_string())
        os.remove('mashup.zip')
    return render_template('index.html')
if __name__=='__main__':
    serve(app,host='127.0.0.1',port=5000)