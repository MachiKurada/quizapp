

class Card:
    def __init__(self, question: str, answer: str)->None:
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"q:{self.question}/a:{self.answer}"