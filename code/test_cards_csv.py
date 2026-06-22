import unittest
from cards import Card, csv_string_to_cards, convert_csv_into_cards

class TestCsvStringToCards(unittest.TestCase):
    def test_happy_path_csv_to_cards(self):
        good_csv = "red,rouge\nblue,bleu\ngreen,vert"
        good_cards = [Card("red", "rouge"), Card("blue", "bleu"), Card("green", "vert")]
        self.assertEqual(csv_string_to_cards(good_csv), good_cards)
    def test_edge_cases_csv_to_cards(self):
        solo_csv = "yellow,jaune"
        solo_card = [Card("yellow", "jaune")]
        self.assertEqual(csv_string_to_cards(solo_csv), solo_card)
        #empty string
        empty_csv = ""
        empty_card = []
        one_empty_line = "orange,orange\n\npurple,violet"
        one_empty_card = [Card("orange", "orange"), Card("purple", "violet")]
        self.assertEqual(csv_string_to_cards(empty_csv), empty_card)
        self.assertEqual(csv_string_to_cards(one_empty_line), one_empty_card)
        #no comma on a line
        not_csv = "La vie en couleur\nLife in color"
        self.assertEqual(csv_string_to_cards(not_csv), empty_card)
        one_wrong_line_csv = "pink,rose\nwtf is perwinkel\n"
        one_wrong_line_cards = [Card("pink", "rose")]
        self.assertEqual(csv_string_to_cards(one_wrong_line_csv), one_wrong_line_cards)
        #too much commas on a line
        three_commas_one_line_csv = "brown, marron, beige"
        self.assertEqual(csv_string_to_cards(three_commas_one_line_csv), empty_card)
        first_line_too_much_commas = "pretty, joli, charmant, mignon, beau\nblack,noir\n"
        too_much_commas_one_card = [Card("black", "noir")]
        self.assertEqual(csv_string_to_cards(first_line_too_much_commas), too_much_commas_one_card)

class TestCsvToCards(unittest.TestCase):
    def test_convert_csv_into_cards(self):
        path = "./cards/base_test_cards.csv"
        cards = [
            Card("red", "rouge"),
            Card("blue", "bleu"), 
            Card("green", "vert"), 
            Card("yellow", "jaune"), 
            Card("orange", "orange"), 
            Card("purple", "violet"),
            Card("pink", "rose"),
            Card("black", "noir")
            ]
        self.assertEqual(convert_csv_into_cards(path), cards)
    




if __name__ == "__main__":
    unittest.main()