import operator
import sys
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cv2
import pyautogui as pg
import instaloader
import pyperclip
import pyttsx3
import requests
import self
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
from requests import get
import webbrowser
import pywhatkit as kit
import smtplib  # smtp library
from email.message import EmailMessage  # for structuring the email message.
import pyjokes
import pyautogui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie  # gif is running through this
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from frontend1 import Ui_Form
from bs4 import BeautifulSoup
from twilio.rest import Client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
'''voices[0].id gives the voice of TTS_MS_EN-US_DAVID_11.0 
if voices[1] is there then it will gives the voice of TTS_MS_EN-US_ZIRA_11.0 '''


# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning")
    elif 12 < hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. Please tell me how can I help you ?")


def whatsapp_msg(self):
    speak("To whom you want to send the message?")
    name = self.take_command()
    number = whatsapp_contact[name]
    speak(f"What message you want to send to {name} ?")
    content = self.take_command()
    speak("At what time you want to send the message? Set the time in 24 hour format.")
    try:
        kit.sendwhatmsg(f"+91{number}", f"{content}", int(input()), int(input()))
    except Exception as e:
        speak("Say that again please...")
        return "none"


whatsapp_contact = {
    'Vidhi': '9340472802',
    'Vanshu': '7667523751',
    'Asmita': '6205295672'
}


# To print news
def news():
    # take a news from newsapi.org
    main_url = 'http://newsApi.org/v2/top-headlines?sources=techcrunch&apiKey=fbbd37c231c24e5c975818ba687c7ab7'
    # print(main_page)
    main_page = requests.get(main_url).json()
    # store articles in variable
    article = main_page["articles"]

    # empty list
    head = []
    day = ["First", "Second", "Third", "Fourth", "Fifth"]
    for ar in article:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"Today's {day[i]} news is: {head[i]}")


def read():
    pg.hotkey("ctrl", 'c')
    tobespoken = pyperclip.paste()
    speak(tobespoken)


# To send email
def send_email(receiver, subject, body):
    # for sending the email
    # server name and the port no.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # start tls-transport layer security that means we are telling or
    # assuring the server that I am very secretive person u can trust me.
    server.starttls()
    # login detail of sender
    server.login('your.email@gmail.com', 'password')
    email = EmailMessage()
    email['from'] = 'your.email@gmail.com'
    email['To'] = receiver
    email['subject'] = subject
    email.set_content(body)
    server.send_message(email)
    # server.sendmail(sender,receiver,content) for single mail


# email list dict to store the email by appropriate name
email_list = {
    'Friend1': 'friend1.email@gmail.com',
    'Friend2': 'friend2.email@gmail.com',
    'Friend3': 'friend3.email@gmail.com',
    'Friend4': 'friend4.email@gmail.com'
}


# To setup the attachment
def send_email_file(receiver, subject, body, file_location):
    msg = MIMEMultipart()
    msg['from'] = 'your.email@gmail.com'
    msg['To'] = receiver
    msg['subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    # setup the attachment
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-disposition', "attachment; filename= %s" % filename)
    # attach the attachment to the MIMEMultipart object
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your.email@gmail.com', 'password')
    server.send_message(msg)


# For getting info about the email to whom it should send
def get_email_info():
    #  subject and the content of the email from user
    speak("To whom you want to send email ?")
    name = self.take_command()
    receiver = email_list[name]
    print(receiver)
    speak("What is the subject of your email ?")
    subject = self.take_command()
    speak("What is the body of your email ?")
    body = self.take_command()
    if "Send a file" in body:
        speak("Please enter the correct path of the file into the shell")
        file_location = input("Enter the path here")
        send_email_file(receiver, subject, body, file_location)
        speak("Please wait, I am sending the mail now.")

    else:
        send_email(receiver, subject, body)
        speak("Please wait, I am sending the mail now.")
    speak("Do you want to send more email ?")
    send_more = self.take_command()
    if 'yes' in send_more:
        # if we say yes the get_email_info function again run
        get_email_info()


# Put your contacts and their data


contact_name = {'Contact1': '+911234567890',
                'Contact2': '+910123456789'}


def twilio_send_msg(self):
    account_sid = 'ACac4fbcdc5da50c28d3d95172526f8594'
    auth_token = 'dff5dd3057f95af410708174c9c8e83f'

    client = Client(account_sid, auth_token)
    speak("To whom you want to send message ?")
    contact = self.take_command()
    number = contact_name[contact]

    try:
        speak("Please tell the content.")
        body = self.take_command()

        client.messages.create(body=body,
                               from_='+16515040964',
                               to=number
                               )
        speak("Message sent")
    except:
        speak(f"No contact named {contact} in my database")


def twilio_call(self):
    global contact_name

    account_sid = 'ACac4fbcdc5da50c28d3d95172526f8594'
    auth_token = 'dff5dd3057f95af410708174c9c8e83f'

    client = Client(account_sid, auth_token)
    speak("To whom you want to send message ?")
    contact = self.take_command()
    number = contact_name[contact]
    try:
        speak(f"Trying to call {contact}")
        call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                                   to=number,
                                   from_='+16515040964'
                                   )
    except:
        speak(f"Seems like you have not registered the contact in my data base so, I cant call {contact}")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        # self.Task_Execution()
        speak("Please say hi or wakeup to continue")
        while True:
            self.query = self.take_command()
            if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
                speak("Starting Engine")
                speak("Collecting required resources")
                speak("Initializing")
                speak("Getting information from the CPU")
                speak("Contacting with mail services")
                self.Task_Execution()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:  # our microphone use as a source it take command from user.
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')  # recognize_google()=Google Web Speech API
            print(f"User said: {query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query

    def Task_Execution(self):
        wish()
        while True:
            self.query = self.take_command().lower()
            # Open notepad by open module
            if "open notepad" in self.query:
                path = "C:\\windows\\system32\\notepad.exe"
                os.startfile(path)
            elif "copy" in self.query:
                pg.hotkey('ctrl', 'c')
                speak('Text copied to clipboard')

            elif "paste" in self.query:
                pg.hotkey('ctrl', 'v')

            elif "undo" in self.query:
                pg.hotkey('ctrl', 'z')

            elif "redo" in self.query:
                pg.hotkey('ctrl', )

            elif "save" in self.query:
                pg.hotkey('ctrl', 's')

            elif "back" in self.query:
                pg.hotkey('browserback')

            elif "go up" in self.query:
                pg.hotkey('pageup')

            elif "go to top" in self.query:
                pg.hotkey('home')

            elif "read" in self.query:
                try:
                    read()
                except:
                    speak("No text selected please select a text")

            elif "who created you" in self.query:
                speak("I was created by Vidhi and Manasi")

            elif "who made you" in self.query:
                speak("I was created by Vidhi and Manasi ")

            elif "how were you developed" in self.query:
                speak("Sorry. I am not allowed to reveal all my secrets.")
            elif "open my sent mail" in self.query:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#sent")
            elif "open a new incognito window" in self.query:
                        pg.hotkey('ctrl','shift','n')
            elif "how are you developed" in self.query:
                speak("Sorry. I am not allowed to reveal all of my secrets.")
            elif "who is Manasi " in self.query:
                speak("Manasi is my developer my teacher the one who taught me how be a good wise smart and a intelligent person Dragonspyder was previously his name And since he left the hacking world he gave this name to me and started programming with python then created me  Now I Am proud to be dragonspyder at last  ")
            elif "who is Vidhi " in self.query:
                speak("Vidhi is my developer my teacher the one who taught me how be a good wise smart and a intelligent person Dragonspyder was previously his name And since he left the hacking world he gave this name to me and started programming with python then created me  Now I Am proud to be dragonspyder at last  ")
            elif "good morning" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Good morning, it is {strTime} now, Hope you had a good sleep.")
            elif "good night" in self.query:
                strTime = datetime.datetime.now().strftime("%X").replace(":", " ")
                gtime = strTime.replace(":", " ")
                speak(f"Good night, it is {gtime} sweat dreams..")
            elif "open my inbox" in self.query:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
            # To open adobe reader
            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
                os.startfile(apath)
            # Open different editors by os module
            elif "open Editor" in self.query:
                speak("Which editor you want to open ?")
                editor = self.take_command().lower()
                if "vs code" in editor:
                    path = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
                    os.startfile(path)
                elif "pycharm" in editor:
                    path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe"
                    os.startfile(path)
            # Open command prompt by os module
            elif "open command prompt" in self.query:
                os.system("start cmd")
            # To open skype
            elif "open skype" in self.query:
                path = "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"
                os.startfile(path)
            # To open camera
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)

                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(0)
                    if k == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            # To play offline music
            elif "play music" in self.query:
                music_dir = "C:\\Users\\MANASI\\Desktop\\Jarvis\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)  # play random songs
                os.startfile(os.path.join(music_dir, rd))
            # To find ip address
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your ip address is {ip}")
            # To search Wikipedia
            elif "wikipedia" in self.query:  # search in wikipedia by wikipedia module
                speak("Searching wikipedia......")
                query = self.query.replace("Wikipedia", " ")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
                print(results)
            # Social browsing
            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")
            elif "open twitter" in self.query:
                webbrowser.open("www.twitter.com")
            elif "open instagram" in self.query:
                webbrowser.open("www.instagram.com")
            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")
            elif "open google" in self.query:
                speak("What should I search on google ?")
                search = self.take_command().lower()
                webbrowser.open(f"{search}")
            # Sending msg on different social media platform
            elif "send message" in self.query:
                whatsapp_msg(self)
            # Send email
            elif "send email" in self.query:
                get_email_info()
            # Play music on youtube
            elif "play music on youtube" in self.query:
                speak("Which song you want to listen on youtube ?")
                song_name = self.take_command().lower()
                kit.playonyt(f"{song_name}")
            # To close any application
            elif "close notepad" in self.query:
                speak("Closing notepad")
                os.system("taskkill /f /im notepad.exe")
            # To set an alarm
            elif "set alarm" in self.query:
                speak("Please tell me the time to set the alarm. For example, set alarm to 5:30am")
                tt = self.take_command()  # set alarm to (time)
                tt = tt.replace("set alarm to ", "")  # 5:30a.m
                tt = tt.replace(".", "")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)
            # To find the jokes
            elif "tell me a joke" in self.query:
                jokes = pyjokes.get_jokes()
                speak(jokes)
            # To shut down the system
            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")
            # To restart the system
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            # To sleep the system
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dil,SetSuspendState 0,1,0")
            # Switch the tab or window
            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            # Tell the news
            elif "tell the news" in self.query:
                speak("Please wait, fetching the latest news.")
                news()
            # Location
            elif "Location" in self.query or "Where are we ?" in self.query:
                speak("Wait, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()  # screp the data in json and in json it is in form of dict.
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state]
                    country = geo_data['country']
                    speak(f"I think we are in {city} city of {country} country")
                except Exception as e:
                    speak("Sorry , Due to network problem I am not able to find where we are.")
                    pass
            # To download instagram profile photo
            elif "instagram profile" in self.query or "insta profile" in self.query:
                speak("Please enter the username correctly")
                name = input("Enter the name: ")
                webbrowser.open(f"www.instagram.com/{name}")
                time.sleep(5)
                speak("Would you like to download the profile picture of this account.")
                condition = self.take_command().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("Task is done, profile picture is saved in our main folder")
                else:
                    pass
            # To take a screenshot
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("Please tell me the name for this screenshot file")
                name = self.take_command().lower()
                speak("Please hold the screen for few seconds , i am taking the screenshot")
                img = pyautogui.screenshot(f"{name}.png")
                speak("Task is done, profile picture is saved in our main folder")

            # Play games
            elif "play games" in self.query or "play game" in self.query:
                speak("Which game you want to play from the given list ?")
                print("Snake\nTic-Tac-Toe")
                game = self.take_command()
                if "s" in game:
                    import snakegame
                    snakegame.playsnake()
                    speak("What you want to do now ?")
                elif "t" in self.query:
                    import tictaktoe
                    tictaktoe.playtictaktoe()
            elif "Are you there ?" in self.query:
                speak("I am always here for your help, please tell me what can I do.")
            # Mathematical calculations
            elif "Do calculations" in self.query or "Can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("What do you want to calculate, example: 3 plus 3")
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divide': operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, ope, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(ope)(op1, op2)

                speak("Your result is: ")
                speak(eval_binary_expr(*(my_string.split())))
            # Make a folder
            elif "create a new folder" in self.query:
                speak("Should I create this folder in your main directory ?")
                drive0 = self.take_command()
                if "yes" in drive0:
                    speak("Please tell the name for a new folder")
                    f_name1 = self.take_command()
                    path = 'E:\\MANASI'
                    os.chdir(path)
                    os.makedirs(f_name1)
                    speak(f"Done, the {f_name1} named folder is created in your main directory")
                elif "no" in drive0:
                    speak("Where you want to create a folder, in desktop or in c drive ?")
                    drive = self.take_command()
                    if "desktop" in drive:
                        speak("Please tell the name for a new folder")
                        f_name = self.take_command()
                        speak("Creating a new folder in desktop, please wait.")
                        path = 'C:\\Users\\MANASI\\Desktop'
                        os.chdir(path)
                        os.makedirs(f_name)
                        speak(f"Done, the {f_name} named folder is created in your desktop")
                    elif "c drive" in drive:
                        speak("You want to create the folder particularly in c drive or anywhere else under c drive ?")
                        drive2 = self.take_command()
                        if "in c drive" in drive2:
                            speak("Please tell the name for a new folder")
                            f_name2 = self.take_command()
                            speak("Creating a new folder in desktop, please wait.")
                            path = 'C:\\Users\\MANASI'
                            os.chdir(path)
                            os.makedirs(f_name2)
                            speak(f"Done, the {f_name2} named folder is created in your desktop")
                        elif "under c drive" in drive2:
                            speak(
                                "If you want to save under c drive in which directory you want to create a new folder ?")
                            drive1 = self.take_command()
                            if "PycharmProject" in drive1:
                                speak("Please tell the name for a new folder")
                                f_name3 = self.take_command()
                                speak("Creating a new folder in desktop, please wait.")
                                path = 'C:\\Users\\MANASI\\PycharmProjects'
                                os.chdir(path)
                                os.makedirs(f_name3)
                else:
                    speak("I can't hear please say it again")

                # To stop JARVIS
            elif "Bye Jarvis" in self.query:
                speak("Thank you for using me. Have a good day.")
                sys.exit()


startExecution = MainThread()


# ui ko interface krne ke liyee
class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # perform action on buttons
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\MANASI\\Desktop\\Jarvis\\GUI\\roundgif.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\MANASI\\Desktop\\Jarvis\\GUI\\Jarvis Loading Screen gif.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\MANASI\\Desktop\\Jarvis\\GUI\\earthgif.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.timeout.connect(self.read_temp)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(f"  Date: {label_date}")
        self.ui.textBrowser_4.setText(f"  Time: {label_time}")

    def read_temp(self):
        search = "Temperature in Nagpur"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        self.ui.textBrowser_5.setText(f"Temperature: {temp}")


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
