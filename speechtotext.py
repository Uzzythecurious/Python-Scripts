import speech_recognition as sr
r  = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now")
    r.energy_threshold = 4000
    audio = r.listen(source) #Starts Listening
    print("Thanks")
try:
    text = r.recognize_google(audio) #Recognizes audio in English 
    print(text)
except: #When there is no notable speech
    print("Sorry, couldn't hear you!")
