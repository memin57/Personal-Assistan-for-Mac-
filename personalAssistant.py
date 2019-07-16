from gtts import gTTS
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import time
from datetime import datetime

def talkToMe(audio):

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def myCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Say Something")
                audio = r.listen(source)
                print("Time Over Thanks")

        try:
                command = r.recognize_google(audio).lower()
                print("Text: " + command)
                return command
        except:
                pass
def search():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                talkToMe('what do you want to search')
                audio = r.listen(source)
                print("Time Over Thanks")

        try:
                print("Text: " + r.recognize_google(audio).lower())
                return r.recognize_google(audio).lower()
        except:
                pass

def assistant(command):
        if command =="what time is it":
            localtime = time.localtime(time.time())
            #print ("Local current time :", localtime)
            Time = str(localtime.tm_hour) +" "+ str(localtime.tm_min)
            talkToMe(Time)
                        
        elif command == "open google":
            word = search()
            url = 'http://www.google.com/#q='
            newWord = url + word
            webbrowser.open(newWord)
                
        elif command == "jarvis" or command == "are you there":
            talkToMe('yes sir')
                      
        elif command == "how are you":
            talkToMe('ı feel great, sir')

        elif command == "what is your name":
            talkToMe('jarvis')
                      
        elif command == "what is the date":
            timestamp = 1528797322
            date_time = datetime.fromtimestamp(timestamp)
            d = date_time.strftime("%d %b, %Y")
            talkToMe(d)

        elif command == "open youtube":
            url = 'https://www.youtube.com/'
            webbrowser.open(url)
                
        elif command == "close safari":
            os.system("pkill Safari")

while True:
    assistant(myCommand())
