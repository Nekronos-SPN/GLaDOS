"""
@Author: Eduardo Rodríguez Sánchez
GLaDOS Voice
"""
from tts import voice

text = voice.listen()
voice.talk(text)