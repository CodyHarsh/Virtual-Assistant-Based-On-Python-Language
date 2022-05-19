import requests
import sys
from email.mime import audio
from fnmatch import translate
from mimetypes import init
from numpy import take
import pyttsx3
import speech_recognition as sr
import spotipy
import json
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
from sqlalchemy import null
from googletrans import Translator
import wikipedia
import googletrans
import os
import pyautogui
import wikipedia as googleScrap
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
from tracemalloc import start
#for qt designer:
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from last import Ui_jarviUi


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices)
engine.setProperty('rate',300)
lang = 1
gt = googletrans.Translator()

def Speak(Audio):
    print(f": {Audio}")
    if lang == 2:
        text = gt.translate(audio,dest='hi')
        audio = text.text
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!!")
        
    elif hour>=12 and hour<18:
        Speak("Good Afternoon!!")
        
    else:
        Speak("Good Evening!!")
        
    Speak("I am jarvis. Please tell me how may I help you")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        self.taskExe()

    def takecommand(self): 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("          ")
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            self.query = r.recognize_google(audio, language='en-in')
            print(f"Your Command :  {self.query}\n")

        except:   
            return "kuchnahi"
            
        return self.query.lower()

    def TakeHindi(self):

        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                self.query = command.recognize_google(audio,language='hi-in')
                print(f"You Said : {self.query}")

            except:
                Speak("Error...")
                print("Network Connection Error!")
                return "none"

            return self.query  

    def taskExe(self) :
        wishMe()

        def OpenApps():
            Speak("Ok Sir , Wait A Second!")
            
            if 'code' in self.query:
                os.startfile("E:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

            elif 'telegram' in self.query:
                os.startfile("E:\\Applications\\Telegram Desktop\\Telegram Desktop\\Telegram.exe")

            elif 'chrome' in self.query:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            
            elif 'facebook' in self.query:
                webbrowser.open('https://www.facebook.com/')

            elif 'instagram' in self.query:
                webbrowser.open('https://www.instagram.com/')

            elif 'maps' in self.query:
                webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

            elif 'youtube' in self.query:
                webbrowser.open('https://www.youtube.com')

            Speak("Your Command Has Been Completed Sir!")
        
        def Temp():
            Speak("Which location temprature you want to find ?")
            search = self.takecommand()
            url = f"https://www.google.com/search?q=weather+{search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature Outside Is {temperature} celcius")

        def CloseAPPS():
            Speak("Ok Sir , Wait A second!")

            if 'youtube' in self.query:
                os.system("TASKKILL /F /im Chrome.exe")

            elif 'chrome' in self.query:
                os.system("TASKKILL /f /im Chrome.exe")

            elif 'telegram' in self.query:
                os.system("TASKKILL /F /im Telegram.exe")

            elif 'code' in self.query:
                os.system("TASKKILL /F /im code.exe")

            elif 'instagram' in self.query:
                os.system("TASKKILL /F /im chrome.exe")
                
            Speak("Your Command Has Been Succesfully Completed!")

        def YoutubeAuto():
            Speak("Whats Your Command ?")
            comm = self.takecommand()

            if 'pause' in comm:
                keyboard.press('space bar')

            elif 'restart' in comm:
                keyboard.press('0')

            elif 'mute' in comm:
                keyboard.press('m')

            elif 'skip' in comm:
                keyboard.press('l')

            elif 'back' in comm:
                keyboard.press('j')

            elif 'full screen' in comm:
                keyboard.press('f')

            elif 'film mode' in comm:
                keyboard.press('t')

            Speak("Done Sir")

        def ChromeAuto():
            Speak("Chrome Automation started!")

            command = self.takecommand()

            if 'close this tab' in command:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in command:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in command:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in command:
                keyboard.press_and_release('ctrl +h')

        def screenshot():
            Speak("Ok Boss , What Should I Name That File ?")
            path = self.takecommand()
            path1name = path + ".png"
            path1 = "C:"+ path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("C:")
            Speak("Here Is Your ScreenShot") 

        while True:
            self.query = self.takecommand()
            ans = self.query
            class Main1(QMainWindow):
                def __init__(self):
                    super().__init__()
                    self.ui = Ui_jarviUi()
                    self.ui.setupUi(self)
                    self.ui.textBrowser_4.setText(ans)

            
            if 'hello' in self.query:
                Speak("Hello Sir , I Am Jarvis .")
                Speak("Your Personal AI Assistant!")
                Speak("How May I Help You?")

            elif 'how are you' in self.query:
                Speak("I Am Fine Sir!")
                Speak("Whats About YOU?")

            elif 'you need a break' in self.query:
                Speak("Ok Sir , You Can Call Me Anytime !")
                Speak("Just Say Wake Up Jarvis!")
                break

            elif 'youtube search' in self.query:
                Speak("OK sIR , This Is What I found For Your Search!")
                self.query = self.query.replace("jarvis","")
                self.query = self.query.replace("youtube search","")
                web = 'https://www.youtube.com/results?search_self.query=' + self.query
                webbrowser.open(web)
                Speak("Done Sir!")

            elif 'website' in self.query:
                Speak("Ok Sir , Launching.....")
                self.query = self.query.replace("jarvis","")
                self.query = self.query.replace("website","")
                self.query = self.query.replace(" ","")
                web1 = self.query.replace("open","")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched!")

            elif 'launch' in self.query:
                Speak("Tell Me The Name Of The Website!")
                name = self.takecommand()
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                Speak("Done Sir!")

            elif 'wikipedia' in self.query:
                Speak("Searching Wikipedia.....")
                self.query = self.query.replace("jarvis","")
                self.query = self.query.replace("wikipedia","")
                wiki = wikipedia.summary(self.query,2)
                Speak(f"According To Wikipedia : {wiki}")

            elif 'screenshot' in self.query:
                screenshot()

            elif 'open facebook' in self.query:
                OpenApps()

            elif 'open instagram' in self.query:
                OpenApps()

            elif 'open maps' in self.query:
                OpenApps()

            elif 'open code' in self.query:
                OpenApps()

            elif 'open youtube' in self.query:
                OpenApps()
                
            elif 'open telegram' in self.query:
                OpenApps()

            elif 'open chrome' in self.query:
                OpenApps()

            elif 'close chrome' in self.query:
                CloseAPPS()

            elif 'music' in self.query:
                Speak("Which music you want to play: ")
                command1 = self.takecommand()
                pywhatkit.playonyt(command1)

            elif 'close telegram' in self.query:
                CloseAPPS()

            elif 'close instagram' in self.query:
                CloseAPPS()

            elif 'close facebook' in self.query:
                CloseAPPS()

            elif 'pause' in self.query:
                keyboard.press('space bar')

            elif 'restart' in self.query:
                keyboard.press('0')

            elif 'mute' in self.query:
                keyboard.press('m')

            elif 'skip' in self.query:
                keyboard.press('l')

            elif 'back' in self.query:
                keyboard.press('j')

            elif 'full screen' in self.query:
                keyboard.press('f')

            elif 'film mode' in self.query:
                keyboard.press('t')

            elif 'youtube tool' in self.query:
                YoutubeAuto()

            elif 'close the tab' in self.query:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in self.query:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in self.query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in self.query:
                keyboard.press_and_release('ctrl +h')

            elif 'chrome automation' in self.query:
                ChromeAuto()

            elif 'joke' in self.query:
                get = pyjokes.get_joke()
                Speak(get)

            elif 'repeat my word' in self.query:
                Speak("Speak Sir!")
                jj = self.takecommand()
                Speak(f"You Said : {jj}")

            elif 'my location' in self.query:
                Speak("Ok Sir , Wait A Second!")
                webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

            elif 'alarm' in self.query:
                Speak("Enter The Time !")
                time = input(": Enter The Time :")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        Speak("Time To Wake Up Sir!")
                        playsound('iron.mp3')
                        Speak("Alarm Closed!")

                    elif now>time:
                        break

            elif 'video downloader' in self.query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                Speak("Enter Video Url Here !")
                Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
                link = StringVar()
                Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
                Entry(root,width = 70,textvariable = link).place(x=32,y=90)

                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.first()
                    video.download()
                    Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

                Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

                root.mainloop()
                Speak("Video Downloaded")
            
            elif 'remember that' in self.query:
                remeberMsg = self.query.replace("remember that","")
                remeberMsg = remeberMsg.replace("jarvis","")
                Speak("You Tell Me To Remind You That :"+remeberMsg)
                remeber = open('data.txt','w')
                remeber.write(remeberMsg)
                remeber.close()

            elif 'what do you remember' in self.query:
                remeber = open('data.txt','r')
                Speak("You Tell Me That" + remeber.read())

            elif 'google search' in self.query:
                self.query = self.query.replace("jarvis","")
                self.query = self.query.replace("google search","")
                self.query = self.query.replace("google","")
                Speak("This Is What I Found On The Web!")
                pywhatkit.search(self.query)

                try:
                    result = googleScrap.summary(self.query,2)
                    Speak(result)

                except:
                    Speak("No Speakable Data Available!")

            elif 'how to' in self.query:
                Speak("Getting Data From The Internet !")
                op = self.query.replace("jarvis","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                Speak(how_to_func[0].summary)
                
            elif 'temperature' in self.query:
                Temp()
            
            elif 'exit' in self.query:
                Speak("Thanks for giving me your time")
                exit()

            elif self.query != 'kuchnahi':
                Speak("This Is What I Found On The Web!")
                pywhatkit.search(self.query)
                try:
                    result = googleScrap.summary(self.query,2)
                    Speak(result)
                    Speak("Here is your best result on the web")
                except:
                    Speak("No Speakable Data Available!")

            else:
                    Speak("Do you have any doubt ? If not speak exit to get exitted from this assistant.")
                    ren = self.takecommand()
                    if(ren == 'exit'):
                        exit()
                    
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarviUi()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)


    def startTask(self):
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
