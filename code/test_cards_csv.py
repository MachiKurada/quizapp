import unittest
from cards import Card, csv_string_to_cards

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
        #no comma on a line
        #too much commas on a line




if __name__ == "__main__":
    unittest.main()