import os

import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import datetime
import smtplib

contacts = {}

# get voice from microsoft
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# selecting type of voice
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning")

    elif 12 <= hour < 18:
        speak("good Afternoon")
    else:
        (speak("good evening"))

    speak(" i am maya sir. please tell me how may i help you")


# take  commends from mic and writtens string output
def takeCommend():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing... ")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said : {query}\n")
    except Exception as error:
        # print(error)
        print("say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('dnyaneshwar1997g@gmail.com','pass')
    server.sendmail('dnyaneshwar1997g@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommend().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia|")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = "C:\\Users\\Dnyaneshwar\\Music\\earl nightingale"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open  code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'salary' in query:
            speak('never')

        # elif 'email to danny':
        #     try:
        #         speak('what should i try')
        #         content = takeCommend()
        #         to = "dannyyourEmail@gmail.com"
        #         sendEmail = (to,content)
        #         speak("Email has been sent!")
        #     except Exception as error:
        #         print(error)
        #         speak("sorry i'm not able to send the mail")



