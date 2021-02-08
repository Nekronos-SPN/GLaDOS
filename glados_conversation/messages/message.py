"""
@Author: Eduardo Rodríguez Sánchez
Messages class and methods
"""
class Message:
    def __init__(self, trigger:str, moods):
        self.trigger = trigger
        # self.ID = self.__get_ID()
        self.answers = {mood: [] for mood in moods}
