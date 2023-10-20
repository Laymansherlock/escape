# 
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()


def say(inputs):
    engine.say(inputs)
    engine.runAndWait()

def command():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "none"
    return query


voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

say("Hello World!")
querys = command()
say("querys")
#check this
engine.stop()
