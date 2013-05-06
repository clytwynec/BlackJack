
class Hand:
	def __init__(self):
		self.cards = []

	def value(self):
		num_aces = 0
		value = 0
		for card in self.cards:
			if card[0] == "A":
				num_aces += 1
			elif card[0] ==  "J" or card[0] ==  "Q" or card[0] ==  "K" or card[0] ==  "10":
				value += 10
			else:
				value += int(card[0])
		if num_aces > 0:
			count = num_aces 
			while count > 0:
				if value > 10:
					value += 1
				else:
					value += 11
				count -= 1

		return value
		

	def add_card(self, card):
		self.cards.append(card)
