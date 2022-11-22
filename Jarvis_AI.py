import pyttsx3  # pyttsx3 is a text-to-speech conversion library in Python
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import random
import smtplib

# Create a dictionary of clients TO send Emails
clients = {
    "arisha": "xxxx349@gmail.com",
    "shery": "xxxx7789@gmail.com",
    "farid":"yyut23@gmail.com"
}

# (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # To take voices
engine.setProperty('voice', voices[1].id)


# Jaris need something to speak so we will make a function (speak) through this function jarvis will speak when it will get any arguement.
def speak(audio):
    engine.say(audio)  # In Audio it is: I am jarvis and I am your AI Assistant
    engine.runAndWait()

# create function wishMe TO wish the user according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")

    elif hour >= 16 and hour < 24:
        speak("Good Evening")

    speak("Hello Mam I am Your AI Assistant Please tell me how may I help You   ")

# THis function will takes microphone input from the user and returns string output
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query #yuxpaqbrxmywsfae

#function to send EMails to user by module smtplib
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('my-gmail', "my-password") # Enter Your Gmail and password
    server.sendmail('my-gmail', to, content) 
    server.close()


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        # Logics for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Areesha\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f" sir the time is {strTime}")

        elif "open drive" in query:
            webbrowser.open('drive.google.com')

        elif 'open gmail' in query:
            webbrowser.open('mail.google.com')

        elif 'open code' in query:
            excel = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office"
            os.startfile(excel)

        elif 'open office' in query:
            webbrowser.open('www.office.com')

        elif 'send email' in query:
            try:
                speak("Enter Your client Name")
                name = input("Enter Your client Name:")
                if name in clients:
                    speak("what should i say")
                    content = takeCommand()
                    to = clients[name]
                    sendEmail(to, content)
                    speak("Email has  been sent! Thank You")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
    
        elif 'quit' in query:
            quit()

