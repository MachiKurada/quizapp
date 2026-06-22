from cards import Card

class Deck:
    def __init__(self, name: str, cards: list[Card])->None:
        self.name = name
        self.cards = cards
        self.size = len(cards)

    def __repr__(self):
        return f"Deck {self.name} has {self.size} cards."
    
    def __eq__(self, other)->bool:
        return (self.name == other.name) and (self.cards == other.cards)