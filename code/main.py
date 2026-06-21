#this is the program that will run.

from cards import Card, get_csv_content

def main ():
    print(get_csv_content("./cards/base_test_cards.csv"))
    print(get_csv_content("./cards"))

    

main()