import unittest
from deck import Deck

class DeckTest (unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_reset(self):
		# reset deck to contain all cards
		self.deck.reset()

		self.assertEquals(len(self.deck.cards), self.deck.size, "Deck should be "+ str(self.deck.size) +" cards.")
		self.assertTrue((3, 's') in self.deck.cards, " Three of Spades should be included.")
		self.assertFalse((12, 'd') in self.deck.cards, " Twelve of Diamonds should not be included.")

		spades = [ card for card in self.deck.cards if card[1] == 's' ]
		self.assertEquals(len(spades), self.deck.size / 4, "Spades are 1/4 of the deck")

	def test_shuffle(self):
		self.deck.reset()
		self.deck.shuffle()

		self.assertEquals(len(self.deck.cards), self.deck.size, "Deck must stay the same size.")

	def test_deal_card(self):
		self.deck.reset()
		initial_size = self.deck.size
		last_card_in_deck = self.deck.cards[-1]

		card = self.deck.deal_card()
		new_size = self.deck.size

		self.assertEquals(initial_size, new_size + 1, "New Deck is correct size")
		self.assertEquals(last_card_in_deck, card, "Dealt card was at end of deck")

unittest.main()