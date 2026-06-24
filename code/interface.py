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

def get_input()->str:
    return input()

def select_deck (deck_list: list[Deck])->None:
    title = "Select your quiz"
    option_list = []
    for deck in deck_list:
        option_list.append(deck.name)
    choice, index = pick(option_list, title)
    print(choice)
    print(deck_list[index].cards)

def quiz_on_card(input: str, card: Card)->bool:
    if not isinstance(input, str) or not isinstance (card, Card):
        raise TypeError ("Not the proper value types")
    print(card.question)
    user_answer = input
    if user_answer == card.answer:
        print ("Good answer !")
        print (f"Answer: {card.answer}")
        return True
    else:
        print ("Wrong answer !")
        print (f"Answer: {card.answer}")
        return False

