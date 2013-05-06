import random

class Deck:
	def __init__(self, size = 52):
		self.cards = []
		self.size = size

	def reset(self):
		values =  range(2, 11, 1)
		values.extend(['J', 'Q', 'K', 'A'])

		suits = ['s', 'd', 'c', 'h']

		self.cards = [(value, suit) for value in values for suit in suits]

	def shuffle(self):
		random.shuffle(self.cards)

	def deal_card(self):
		card = self.cards.pop()
		self.size -= 1
		
		return  card