class Interpreter:
	arr = []
	fac = 24
	order = 0
	parity = 0
	def sendCard(self, card):
		self.parity += card
		val = sum(map(lambda v: v < card, self.arr))
		self.fac //= len(self.arr) + 1
		self.order += self.fac * val
		self.arr.append(card)
	def calculateHiddenCard(self):
		hiddenCard = 2 * self.order + (self.parity % 2)
		arr = self.arr[:]
		arr.sort()
		for card in arr:
			if hiddenCard >= card: hiddenCard += 1
		return hiddenCard

def send(cardList):
	otherCards = cardList[:]
	otherCards.sort()
	parity = sum(otherCards) % 2
	hidden = otherCards[parity]
	order = (hidden - parity) // 2
	otherCards.remove(hidden)
	all_indices = [0, 1, 2, 3]
	divisors = [(1, 4), (4, 3), (12, 2), (24, 1)]
	indices = []
	for (d, m) in divisors:
		indices.append(all_indices.pop(order // d % m))
	
	i = Interpreter()
	while len(indices):
		i.sendCard(otherCards[indices.pop()])
	print(hidden, "==", i.calculateHiddenCard())

import sys
import random

if sys.argv[1][0] == "r":
	cards = random.sample(range(0, 51), 5)
else:
	cards = list(map(int, sys.argv[1:]))
	
print(cards)
send(cards)
