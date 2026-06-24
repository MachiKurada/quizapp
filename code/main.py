#this is the program that will run.

from decks import Deck, create_deck_list_from_directory
from interface import select_language, select_deck, quiz_on_deck

def main ():
    deck_list = create_deck_list_from_directory("./cards")
    select_deck(deck_list)

    

main()