#Cards
#A K Q J 10 9 8 7 6 5 4 3 2

#Suit
#Diamond (D)
#Hearts (H)
#Spades (S)
#Clubs (C)

#Ace equals 11 or 1, 11 unless hand will >= 21

class Card(object):
	def __init__(self, value, suit):
		self.regVal = value
		self.suit = suit
		if value in ['2','3','4','5','6','7','8','9','10']:
			self.pointVal = int(value)
		if value in ['J','Q','K']:
			self.pointVal = 10
		if value == 'A':
			self.pointVal = 11

	def getVal(self):
		return self.regVal