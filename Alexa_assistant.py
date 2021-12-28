'''
In this project we are going to make the desktop assistance and we are gives simple simple commands.


install modules using the pip install module name
   these are the requires modules
'''

from platform import architecture
import datetime
import speech_recognition as sr
import pyttsx3
import requests
import wikipedia
import webbrowser
import json
import os
import PyWhatKit as kit
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# you can use the 0 for men and the 1 for the women audio

author = "Programmer"  #you can fill your name


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"good morningf {author}")

    elif hour >= 12 and hour < 18:
        print(f"good evening{author}")

    else:
        print(f"good evening {author}")
    speak(f"Hello {author} I am Alexa ,please tell me how may I help you ? ")


def takeCommand():
    '''
    Take inputs from microphone and print it on the  
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language="english")
        print(f"User said : {query}\n")

    except Exception as e:
        print(f"Sorry {author} ,say that again ...")
        return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.echlo()
    server.starttls()
    server.login('your gmail address',
                 'your password')  #fill password and gmail address

    server.sendmail('your gamil address', to, content)
    server.close()


if __name__ == '__main__':
    # speak(f"Welcome {author} ,I am alexa")
    wishMe()

    while True:
        query = takeCommand().lower()
        if "wikipedia" and "who" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'news' in query:  # to use this functon create your api key for that use website as    news api
            speak("News Headlines")
            query = query.replace("news", "")
            #get api
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c8d84379c4d043ea9231d8cef05810a2"
            news = requests.get(url).text
            news = json.load(news)
            art = news['articles', ]
            for article in art:
                print(article['title'])
                speak(article['title'])
                print(article['description'])
                speak(article['description'])
                speak("Moving to next news")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "search browser" in query:
            speak("what should i search")
            um = takeCommand().lower()

            webbrowser.open(f"{um}")
        elif "ip address" in query:
            ip = requests.get("https:/api.ipify.org").text
            print(f"your ip is {ip}")
            speak(f"your ip is {ip}")
        elif "open command prompt" in query:
            os.system("start cmd")

        elif 'open code' in query:
            codepath = "C:\\Users\\Sudhir\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'play music' in query:
            music_dir = 'Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play youtube' in query:
            speak("what i search in you tube ?")
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")

        elif 'send message ' in query:  #send message open whatsappp in desktop
            speak("whom do you want to send the message")
            num = input("enter the number")
            speak("what do you want to  send")
            msg = takeCommand().lower()
            speak("please enter time sir")
            H = int(input("enter hour \n"))
            M = int(input("enter the minute \n"))
            kit.sendwhatmsg(num, msg, H, M)

        elif 'send email' in query:  #to send emails make the setting less secure beacuse the gmail is very secure
            speak("What should i send sir")
            content = takeCommand().lower()
            speak("whom to send the email")
            to = input("Enter the email address :\n")
            sendEmail(to, content)

#          ............BEST OF LUCK.......
