from const import *
from random import *
class Stats:
    def __init__(self,questions = QS):
        self.questions  =  questions
        self.total = len(questions)
        self.now = choice(self.questions)
        self.answered = 1
        self.right = 0
    def next_question(self):
        if len(self.questions) == 1:
            self.answered = -1
        else:
            self.questions.remove(self.now)
            self.now = choice(self.questions)
            self.answered + 1