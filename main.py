import random
import subprocess
import sys
import time
from urllib.request import urlopen
from googletrans import Translator
import psutil
import pywhatkit
import speech_recognition as sr
import win32com.client as wincl
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup, BeautifulSoup
import datetime
import pyjokes
import tkinter
import webbrowser

import pyttsx3
import winshell

import wolframalpha

import requests
import json

import os.path

from playsound import playsound
from pytube import YouTube
from pywikihow import search_wikihow
from wikipedia import wikipedia

client = wolframalpha.Client('E8U3YY-U9X2HYVY83')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Music():
    speak("Tell Me The NamE oF The Song!")
    musicName = takeCommand()

    if 'soviet' in musicName:
        os.startfile('C:\\Users\\PC\\Music\\national\\01_USSR.mp3')

    elif 'old' in musicName:
        os.startfile('C:\\Users\\PC\\Music\\national\\YoureAGrandOldFlag.mp3')

    elif 'usa' in musicName:
        pywhatkit.playonyt('C:\\Users\\PC\\Music\\national\\national usa nonvoc.mp3')


    else:
        pywhatkit.playonyt(musicName)

    speak("Your Song Has Been Started! , Enjoy Sir!")

def news():
    url = "https://www.khaleejtimes.com"
    client = ureq(url)
    print(client)
    page_html = client.read()
    print(page_html)
    client.close()
    page_soup = soup(page_html, "html.parser")
    articles = page_soup.find("div", {"class": "view-content"})
    articles = articles.findAll("div", {"class": "catagory-listing"})
    i = 1

    for x in articles:
        title = x.find("h2").text
        para = x.find("p").text
        print(i, title, "\n", "\n", para, "\n", "\n")
        speak(title)
        speak(para)
        i = i + 1

    def Temp():
        search = "temperature in ajman"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        speak(f"The Temperature Outside Is {temperature} celcius")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takeCommand()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            speak(f"The Temperature in {name} is {temperature} celcius")


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am amigos Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def cpu():
    usage = str(psutil.cpu_percent())  # tell about cpu usage
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def Takede():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio, language='de')
            print(f"You Said : {query}")

        except:
            return "none"

        return query.lower()


def TakeHindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio, language='hi')
            print(f"You Said : {query}")

        except:
            return "none"

        return query.lower()


def Tran_hi():
    speak("Tell Me The Line!")
    line = TakeHindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)


def Tran_de():
    speak("Tell Me The Line!")
    line = Takede()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'music' in query:
            Music()

        elif 'Translate to hindi' in query:
            Tran_hi()

        elif 'Translate to hindi' in query:
            Tran_de()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call(["shutdown", "/s"])

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)



        elif "thank you" in query:
            speak("Your welcome")

        elif 'my location' in query:
            speak("Ok Sir , Wait A Second!")
            webbrowser.open(
                'https://www.google.com/maps/place/@25.3955817,55.4515705,19z/data=!4m5!3m4!1s0x3e5f591d51ad6ea3:0x5c23ecd6be2cc2b7!8m2!3d25.3954662!4d55.4517888')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'alarm' in query:
            speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time To Wake Up Sir!")
                    playsound('music\\USA.mp3')
                    speak("wake up,\nAlarm Closed!")

                elif now > time:
                    pass
        elif 'video downloader' in query:
            root = tkinter.Tk()
            root.geometry('500x300')
            root.resizable(0, 0)
            root.title("Youtube Video Downloader")
            speak("Enter Video Url Here !")
            tkinter.Label(root, text="Youtube Video Downloader", font='arial 15 bold').pack()
            link = tkinter.StringVar()
            tkinter.Label(root, text="Paste Youtube Video URL Here", font='arial 15 bold').place(x=160, y=60)
            tkinter.Entry(root, width=70, textvariable=link).place(x=32, y=90)


            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                tkinter.Label(root, text="Downloaded", font='arial 15').place(x=180, y=210)


            tkinter.Button(root, text="Download", font='arial 15 bold', bg='pale violet red', padx=2,
                           command=VideoDownloader).place(x=180, y=150)

            root.mainloop()
            speak("Video Downloaded")

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that", "")
            remeberMsg = remeberMsg.replace("jarvis", "")
            speak("You Tell Me To Remind You That :" + remeberMsg)
            remeber = open('data.txt', 'w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt', 'r')
            speak("You Tell Me That" + remeber.read())

        elif 'what is' in query or 'where is' in query or 'when is' in query or 'who is' in query:
            import wikipedia as googleScrap

            query = query.replace("amigo", "")
            query = query.replace("what is", "")
            query = query.replace("where is", "")
            query = query.replace("who is", "")
            query = query.replace("when is", "")
            speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query, 2)
                speak(result)

            except:
                speak("No Speakable Data Available!")

        elif 'how to' in query:
            speak("Getting Data From The Internet !")
            op = query.replace("jarvis", "")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif 'battery' in query:
            cpu()

        elif "log off" in query or "sign out" in query:
            speak("Ok Gokul")
            subprocess.call(["shutdown", "/l"])



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()



        elif 'play music' in query:
            Music()

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif "weather" in query.lower():
            Temp()

        elif 'news' in query:
            news()


        elif 'open python' in query:
            codePath = "C:\\Users\\PC\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif "record" in query:
            rec_audio()

        elif "hi" in query:
            speak("hello, i am amigos how may i be of help")
            print()

        elif "joke" in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            print(My_joke)
            speak(My_joke)

        # elif "" in query:
