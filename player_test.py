import unittest
from player import Player


class playerTest (unittest.TestCase):
	def setUp(self):
		self.player = Player(100)

	def test_add_money(self):
		self.player.add_money(10)
		self.assertEquals(self.player.bank, 110)

	def test_remove_money(self):
		self.player.remove_money(10)
		self.assertEquals(self.player.bank, 90)

	def test_can_play(self):
		self.assertTrue(self.player.can_play(10))
		self.assertTrue(self.player.can_play(100))
		self.assertFalse(self.player.can_play(110))


unittest.main()
