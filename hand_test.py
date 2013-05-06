import unittest
from hand import Hand

class handTest (unittest.TestCase):
	def setUp(self):
		self.hand = Hand()

	def test_value(self):
		self.hand.add_card(('5', 'h'))
		self.assertEquals(self.hand.value(), 5)

		self.hand.add_card(('A', 'd'))
		self.assertEquals(self.hand.value(), 16)

		self.hand.add_card(('J','s'))
		self.assertEquals(self.hand.value(), 16)

		self.hand = Hand()

		self.hand.add_card(("A", "s"))
		self.hand.add_card(("A", "d"))
		self.assertEquals(self.hand.value(), 12)

	def test_add_card(self):
		card =('A', 's')

		self.hand.add_card(card)

		self.assertEquals(len(self.hand.cards), 1)
		self.assertTrue(card in self.hand.cards)

		card2 =('K', 'd')

		self.hand.add_card(card2)

		self.assertEquals(len(self.hand.cards), 2)
		self.assertTrue(card2 in self.hand.cards)




unittest.main()
