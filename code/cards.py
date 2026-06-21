import os

class Card:
    def __init__(self, question: str, answer: str)->None:
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"q:{self.question}/a:{self.answer}"
    

def get_csv_content(file_path: str)->str:
    if os.path.isfile(file_path) and file_path.endswith(".csv"):
        with open(file_path) as f:
            csv_content = f.read()
        return csv_content
    else:
        raise ValueError