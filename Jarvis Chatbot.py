import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')  
engine.setProperty("voice",voice[1].id)

def talk(text):
   engine.say(text)
   engine.runAndWait()


def jarvis_command():  
    try:
       with sr.Microphone() as source: 
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command = command.lower()
            ampm = ampm.lower()
            if "jarvis" in command:
              command = command.replace("jarvis","")  
              print(command) 
            
    except:
        pass
    return command

def run_jarvis():
    command = jarvis_command()
    print(command)
    

    if "play" in command:
        song = command.replace("play","")
        talk("Playing" +song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Current time is"+time)

    elif "businessman" in command:
        person = command.replace("businessman","")
        info = wikipedia.summary(person,5)
        print(info)
        talk(info)  


    elif "cricketer" in command:
        person = command.replace("cricketer","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)  

    elif "superstar" in command:
        person = command.replace("superstar","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info) 
    
    elif "educator" in command:
        person = command.replace("educator","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif "youtuber" in command:
        person = command.replace("youtuber","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    

    elif "singer" in command:
        person = command.replace("singer","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif "revolutionary" in command:
        person = command.replace("revolutionary","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info) 


    elif "president" in command:
        person = command.replace("president","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)     

    elif "joke" in command:
         talk(pyjokes.get_joke())

run_jarvis()                                                                                                                        