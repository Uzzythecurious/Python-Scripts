import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
# name= input("What is your name? ")

engine.say("What is your name?")
engine.runAndWait() 

r  = sr.Recognizer()

with sr.Microphone() as source:
    print("Say your name clealy with oomph")
    r.energy_threshold = 4000
    audio = r.listen(source) #Starts Listening
    print("Thanks")
try:
    text = r.recognize_google(audio) #Recognizes audio in English
    engine.say(f"Hello, {text}, I can't wait to be adapted to do more with audio input!")
    engine.runAndWait() 
    # print(text)
except: #When there is no notable speech
    print("Sorry, couldn't hear you!")





