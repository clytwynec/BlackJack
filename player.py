from hand import Hand


class Player():
	def __init__(self, initial_bank):
		self.hand = Hand()
		self.bank = initial_bank

	def add_money(self, amount):
		self.bank += amount 

	def remove_money(self, amount):
		self.bank -= amount

	def get_move(self):
		1

	def can_play(self, min_bid):
		return self.bank >= min_bid

	def reset_hand(self):
		self.hand = Hand()

	def print_hand(self):
		for card in self.hand.cards:
			print str(card[0]) + str(card[1]),
		print " "
