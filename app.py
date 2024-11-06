import streamlit as st
import speech_recognition as sr

container=st.container()
recognizer=sr.Recognizer()
recognizer.energy_threshold=300

mic=sr.Microphone()
with mic as source:
    st.write("say something")
    audio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(audio)
        st.write(text)
    except sr.UnknownValueError:
        st.write("could not understand")
