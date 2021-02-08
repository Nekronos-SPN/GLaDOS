"""
@Author: Eduardo Rodríguez Sánchez
Listen and Talk
"""
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pathlib import Path

def listen(microphone = sr.Microphone()):
    """Listens to the words said by the user and converts it into a string."""
    r = sr.Recognizer()
    # Gets the default microphone
    with microphone as source:
        # Listens to a command
        audio = r.listen(source)
        try:
            voice_text = r.recognize_google(audio, language="es-ES").capitalize()
        except:
            voice_text = "Lo siento no te he entendido"
    return voice_text
    
def talk(text:str):
    """Text to speech function. Creates an mp3 file and plays it."""
    response = Path("glados_conversation/tts/response.mp3")
    text_to_speech = gTTS(text, lang='es-us')
    # We make sure that a file is created
    with open(response, "wb") as audio:
        text_to_speech.write_to_fp(audio)
    playsound(str(response))

if __name__ == "__main__":
    text = listen()
    talk(text)