#this is the program that will run.

from decks import Deck, create_deck_list_from_directory

def main ():
    print(create_deck_list_from_directory("./cards"))

    

main()