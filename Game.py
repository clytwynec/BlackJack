from Round import Round
from contestant import Contestant 
from dealer import Dealer

class Game:
	def __init__(self):
		self.contestant = Contestant(100)
		self.dealer = Dealer(100)

	def play(self):
		print "Welcome to BlackJack Super Cool Game PlusPlus!"

		while True:
			self.play_round()

			if self.contestant.bank <= 0:
				"You've gone bankrupt! No more money to bid!"
				break

			else:
				answer = raw_input("Would you like to like to play another round? (Y or N)").strip().lower() 

				while answer not in ("y", "n"):
					answer = raw_input("Would you like to like to play another round? (Y or N)").strip().lower() 

				if answer == "n":
					break

		print "Thanks for playing BlackJack Super Cool Game PlusPlus!"


	def play_round(self):
		print "You have " + str(self.contestant.bank) + " dollars in the bank."
		bid = int(raw_input("How many dollars would you like to bet?").strip())

		if bid > self.contestant.bank:
			print "You can't bet more than you have!"
			self.play_round()

		r = Round(self.contestant, self.dealer, bid)
		r.play()

g = Game()
g.play()

		