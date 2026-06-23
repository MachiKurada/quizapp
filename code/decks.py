import os
from cards import Card, convert_csv_into_cards

class Deck:
    def __init__(self, name: str, cards: list[Card])->None:
        self.name = name
        self.cards = cards
        self.size = len(cards)

    def __repr__(self):
        return f"Deck {self.name} has {self.size} cards."
    
    def __eq__(self, other)->bool:
        return (self.name == other.name) and (self.cards == other.cards)
    
def create_deck_from_csv(file_path: str)->Deck:
    if os.path.isfile(file_path) and file_path.endswith(".csv"):
        cards = convert_csv_into_cards(file_path)
        name = os.path.basename(file_path).replace(".csv","")
        return Deck(name, cards)
    else:
        raise ValueError("Not a proper path name")
    
def create_deck_list_from_directory(directory_path: str)->list[Deck]:
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        content_names = os.listdir(directory_path)
        deck_list = []
        for name in content_names:
            content_path = os.path.join (directory_path, name)
            if os.path.isdir(content_path):
                deck_list.extend(create_deck_list_from_directory(content_path))
            else:
                try:
                    deck_list.append(create_deck_from_csv(content_path))
                except ValueError:
                    continue
        return deck_list
    else:
        raise ValueError("Not a valid directory")



