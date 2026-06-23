#this is the program that will run.

from decks import create_deck_from_csv

def main ():
    print(create_deck_from_csv("./cards/base_test_cards.csv"))
    print(create_deck_from_csv("./cards"))

    

main()