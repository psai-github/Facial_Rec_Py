import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from sqlalchemy import false
import wikipedia
import pyjokes
import speech_recognition
from tkinter import *
class alexa:
    def __init__(self,name):
        def answer():
            command=self.text.get()
            if 'play' in command:
                song = command.replace('play', '')
                self.talk('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                self.talk('Current time is ' + time)
            elif 'who is' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                self.talk(info)
            elif 'joke' in command:
                self.talk(pyjokes.get_joke())

            else:
                self.talk("Sorry, I don't know that one.")

        self.name=name
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)


        #GUI

        screen=Tk()
        screen.title("How may I assist you today "+self.name+"?")
        screen.geometry("500x100")
        screen.config(bg="black")



        self.text=Entry(screen,width=25,font=("Impact",25))
        self.text.pack()

        button=Button(screen,text="Submit",width=6,font=("Impact",25),bg="blue",command=answer)
        button.pack()

        
        self.talk("Hi "+self.name+" my name is ExBot")
        self.talk("How may I assist you today?")
        mainloop()

    def talk(self,text):
        self.engine.say(text)
        self.engine.runAndWait()







