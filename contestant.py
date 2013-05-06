from player import Player

class Contestant(Player):
	def __init__(self, initial_bank):
		Player.__init__(self, initial_bank)

	def get_move(self):
		move = raw_input("hit or stay?").strip().lower()

		if move not in ("hit", "stay"):
			move = self.get_move()
		
		return move


	def print_hand(self):
		print " "
		print "Your Hand:  ",
		Player.print_hand(self)