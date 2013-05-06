import unittest
from dealer import Dealer


class dealerTest (unittest.TestCase):
	def setUp(self):
		self.dealer = Dealer(100)

	def test_get_move(self):
		self.assertEquals(self.dealer.get_move(), "hit")

		self.dealer.hand.add_card(("A", "s"))
		self.assertEquals(self.dealer.get_move(), "hit")

		self.dealer.hand.add_card(("3", "d"))
		self.assertEquals(self.dealer.get_move(), "hit")
		
		self.dealer.hand.add_card(("2", "c"))
		self.assertEquals(self.dealer.get_move(), "stay")
		


unittest.main()
