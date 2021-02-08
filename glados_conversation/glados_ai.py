"""
@Author: Eduardo Rodríguez Sánchez
GLaDOS Voice
"""
from tts import voice
from status import gen_info
from messages.message import Message

message1 = Message("NONE", gen_info.moods)
print(message1.answers)

# text = voice.listen()
# voice.talk(text)