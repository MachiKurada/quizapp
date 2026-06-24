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
    quiz_on_deck(deck_list[index])

def quiz_on_card(card: Card)->bool:
    if not isinstance (card, Card):
        raise TypeError ("Not the proper value types")
    print(card.question)
    user_answer = input()
    if user_answer == card.answer:
        print ("Good answer !")
        print (f"Answer: {card.answer}\nYour answer: {user_answer}")
        return True
    else:
        print ("Wrong answer !")
        print (f"Answer: {card.answer}\nYour answer: {user_answer}")
        return False

def quiz_on_deck(deck: Deck)->None:
    print(f"Starting quiz on {deck.name}")
    score = 0
    card_number = 1
    wrong_cards = []
    for card in deck.cards:
        print(f"{card_number}/{deck.size}")
        result = quiz_on_card(card)
        if result:
            score += 1
        else:
            wrong_cards.append(card)
        card_number += 1
        print("")
    print (f"Final score: {score}/{deck.size}")
    print (f"Cards to review : {wrong_cards}")
    print ("Thanks for playing !")
    

