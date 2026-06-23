from pick import pick
from decks import *
from cards import *

#Just a test to see if pick works well:
def select_language ():
    title = "select language"
    options = ["English", "Français", "日本語"]
    choice, index = pick(options, title)
    print(choice)
    print(index)

def select_deck (deck_list: list[Deck])->None:
    title = "Select your quiz"
    option_list = []
    for deck in deck_list:
        option_list.append(deck.name)
    choice, index = pick(option_list, title)
    print(choice)
    print(deck_list[index].cards)
