import speech_recognition as sr 
#import playsound # to play saved mp3 file
#from gtts import gTTS # google text to speech
#import os # to save/open files
#import wolframalpha # to calculate strings into formula
#from selenium import webdriver

rObject = sr.Recognizer()
audio = ''
 
with sr.Microphone() as source:
    print("Speak...")
         
        # recording the audio using speech recognition\
    audio = rObject.listen(source, phrase_time_limit = 5) 
    text = rObject.recognize_google(audio, language ='en-US')
    print("You : ", text)
    print("Stop.")
