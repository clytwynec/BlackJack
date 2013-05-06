from player import Player

class Dealer(Player):
	def __init__(self, initial_bank):
		Player.__init__(self, initial_bank)

		self.played = False
	def reset_hand(self):
		Player.reset_hand(self)
		self.played = False

	def get_move(self):
		if self.hand.value() >= 16:
			self.played = True
			return "stay"
		else:
			self.played = True
			return "hit"

	def print_hand(self):
		print " "
		print "Dealer's Hand:  ",

		if self.played is True:
			Player.print_hand(self)
		else:
			print "XX ",
			print str(self.hand.cards[1][0]) + str(self.hand.cards[1][1])



