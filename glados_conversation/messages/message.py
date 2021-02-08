"""
@Author: Eduardo Rodríguez Sánchez
Messages class and methods
"""
import random
class Message:
    """Message class wich contains all the answers to a given question or the responses
    to a given text"""
    def __init__(self, trigger:str, moods:list):
        self.trigger = trigger
        self.ID = None # self.__get_ID()
        self.answers = {mood: [] for mood in moods}
    
    def __get_ID(self):
        ...
    
    def set_answer(self, mood:str, answer:str):
        """Adds and answer to the dictionary of answers in the Message type object"""
        try:
            self.answers[mood].append(answer)
        except KeyError:
            pass
    
    def get_answer(self, mood:str) -> str:
        """Returns a random answer depending on the mood of the machine"""
        answers = self.answers.get(mood, ["Error en el estado de ánimo. Supervisa gen_info.py"])
        if len(answers) != 0:
            return random.choice(answers)
        else:
            return "Error, no sé la respuesta"


    

