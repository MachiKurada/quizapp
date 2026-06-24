import unittest
from cards import *
from decks import *
from interface import *

class TestQuizOnCard(unittest.TestCase):
    def test_base_right_wrong(self):
        card = Card("rouge", "red")
        self.assertTrue(quiz_on_card("red", card))
        self.assertFalse(quiz_on_card("blue", card))
    def test_edge_input(self):
        card = Card("rouge", "red")
        empty_card = Card("", "")
        not_a_card = "card"
        empty_input = "" 
        not_input = 12
        self.assertTrue(quiz_on_card(empty_input, empty_card))
        self.assertFalse(quiz_on_card(empty_input, card))
        self.assertFalse(quiz_on_card("something", empty_card))
        with self.assertRaises(TypeError):
            quiz_on_card(not_input, card)
        with self.assertRaises(TypeError):
            quiz_on_card("something", not_a_card)


if __name__ == "__main__":
    unittest.main()