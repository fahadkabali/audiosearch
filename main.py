#Packages neccessary for the program to run smoothly
import speech_recognition as sr
from selenium import webdriver

# a class to create the audio recognizer
class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
           try:
                with sr.Microphone() as source:
                    print("SAY SOMETHING")
                    audio = self.recognizer.listen(source,timeout=5,phrase_time_limit=20)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(command)
                    if 'search' in command:
                        driver=webdriver.Chrome()
                        driver.get(f"https://www.google.com/search?q={command.split('search')[-1]}")
           except sr.UnknownValueError:
               pass


listerener = Voice()
