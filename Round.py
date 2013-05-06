from contestant import Contestant
from dealer import Dealer
from deck import Deck

class Round():
	def __init__(self, contestant, dealer, bid):
		self.deck = Deck()
		self.deck.reset()
		self.deck.shuffle()

		self.bid = bid

		self.contestant = contestant
		self.dealer = dealer

		self.players = [self.contestant, self.dealer]

	def initial_deal(self):
		num_cards = 2

		self.contestant.reset_hand()
		self.dealer.reset_hand()

		while num_cards > 0:
			for player in self.players:
				player.hand.add_card(self.deck.deal_card())
			num_cards -= 1

		self.dealer.print_hand()

	def play(self):
		self.initial_deal()

		for player in self.players:
			player.print_hand()

			while player.hand.value() <= 21 and player.get_move() != "stay":
				player.hand.add_card(self.deck.deal_card())	
				player.print_hand()

		self.score_round()

	def score_round(self):
		dealer_score = self.dealer.hand.value()
		contestant_score = self.contestant.hand.value()
		print "Dealer's Score: " + str(dealer_score)
		print "Your Score: " + str(contestant_score)

		if contestant_score > 21:
			self.contestant.remove_money(self.bid)
			print("You went over 21! Lost Round!")

		elif contestant_score == dealer_score:	
			print("You tied! No gains, no losses!")

		elif contestant_score > dealer_score or dealer_score >21:
			print("You won this round!")
			self.contestant.add_money(self.bid)

		elif contestant_score < dealer_score and dealer_score <=21:
			print("You lost this round.")
			self.contestant.remove_money(self.bid)



