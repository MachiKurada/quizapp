import os

class Card:
    def __init__(self, question: str, answer: str)->None:
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"q:{self.question}/a:{self.answer}"
    
    def __eq__(self, other)->bool:
        return (self.question == other.question) and (self.answer==other.answer)
    

def get_csv_content(file_path: str)->str:
    if os.path.isfile(file_path) and file_path.endswith(".csv"):
        with open(file_path) as f:
            csv_content = f.read()
        return csv_content
    else:
        raise ValueError("Not a proper path name")
    
def csv_string_to_cards(csv_string: str)->list[Card]:
    if len(csv_string) == 0:
        return []
    card_list = []
    pre_list = csv_string.split("\n")
    for item in pre_list:
        if len(item) > 0:
            pre_card = item.split(",")
            if len(pre_card) ==2:
                card_list.append(Card(pre_card[0], pre_card[1]))
    return card_list

def convert_csv_into_cards(file_path: str)->list[Card]:
    csv_content = get_csv_content(file_path)
    return csv_string_to_cards(csv_content)