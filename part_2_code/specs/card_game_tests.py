import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game =CardGame
        self.card1 = Card("Club", 7)
        self.card2 = Card("Heart", 10)
        self.card3 = Card("Space", 1)
        self.card4 = Card("Diamond", 6)
        self.cards = [self.card1,self.card2,self.card3,self.card4]

    def test_check_for_ace_false(self):
        is_ace = self.game.check_for_ace(self, self.card1)
        self.assertEqual(False, is_ace)


    def test_check_for_ace_True(self):
        is_ace = self.game.check_for_ace(self, self.card3)
        self.assertEqual(True, is_ace)

    def test_highest_card(self):
        highest = self.game.highest_card(self,self.card1,self.card2)
        self.assertEqual(self.card2, highest)

    def test_highest_card(self):
        highest = self.game.highest_card(self,self.card1,self.card4)
        self.assertEqual(self.card1, highest)

    def test_total_of_cards(self):
        total = self.game.cards_total(self,self.cards)
        self.assertEqual("You have a total of 24", total)

    