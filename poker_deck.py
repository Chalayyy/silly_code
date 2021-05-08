import random

class Card():

	suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

	values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

	# initialize each card

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	# printing card tells value and suit

	def __repr__(self):
		return f"{self.value} of {self.suit}"


class Deck():

	# initialize deck

	def __init__(self):
		self.cards = [Card(v,s) for v in Card.values for s in Card.suits ]
		
	# printing deck tells how many cards remain

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	# count returns current size of deck

	def count(self):
		return len(self.cards)
	
	# _deal deals a number of cards if there are enough/any remaining

	# def _deal(self, num):
	# 	if not self.count():
	# 		raise ValueError("All cards have been dealt")
	# 	hand = []
	# 	actual = min(num, self.count())
	# 	for i in range(actual):
	# 		hand.extend(self.cards.pop())
	# 	return hand

	def _deal(self, num):
		count = self.count()
		actual = min([count,num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	# deals a single card

	def deal_card(self):
		return self._deal(1)[0]

	# deals a number of cards and reveals them

	def deal_hand(self, hand_size):
		return self._deal(hand_size)
		

	# shuffles a full deck

	def shuffle(self):
		if self.count() == 52:
			return random.shuffle(self.cards)
		else:
			raise ValueError("Only full decks can be shuffled")
		

	# player selects how many cards they want to exchange



class Hand():

	def __init__(self, hand_size, deck, player):
		self.card_list = deck.deal_hand(hand_size)
		self.deck = deck
		self.player = player

	def __repr__(self):
		return f"{self.player}'s hand is {self.card_list}"

	# consider using .remove, del
	def exchange(self):
		ex_num = int(input("How many cards do you want to change? "))
		ex = []
		for i in range(0,ex_num):
			ex.append(int(input("Which card do you want to exchange?")))
		ex.sort(reverse=True)
		[self.card_list.pop(element-1) for element in ex]
		new = self.deck.deal_hand(ex_num)
		self.card_list.extend(new) 

	# def exchange(self):
	# 	exchange_amount = int(input("How many cards do you want to change? "))
	# 	# ex = [int(card) for card in input("Which cards do you want to exchange? ").split()]
	# 	lst1 = [int(item) for item in input("Enter the list items : ").split()] 
	# 	for item in lst1[::-1]:
	# 		self.card_list.pop(item-1)
	# 	self.card_list.append(self.deck.deal_hand(exchange_amount))

d = Deck()
d.shuffle()

p1 = Hand(5, d, "Jen")
print(p1)
p1.exchange()
print(p1)

p2 = Hand(5, d, "Charlie")
print(p2)
p2.exchange()
print(p2)

print("Congratulation JENNIFER! You beat CHARLIE")


# Winning_hands = [
# 	"Royal Flush", 
# 	"Straight Flush"
# 	"4 of a Kind", 
# 	"Full House", 
# 	"Flush", 
# 	"Straight", 
# 	"Three of a kind",
# 	"Two Pair"
# 	"Pair",
# 	"High Card"
# 	]

# straights = [set(values.append("A")[s:s+5]) for s in range(0,10)]

# players = [p1,p2]
# for player in players:
# 	hand = None
	
# 	if any(
# 		all(card.suit == "Hearts" for card in player.card_list)
# 		all(card.suit == "Clubs" for card in player.card_list)
# 		all(card.suit == "Spades" for card in player.card_list)
# 		all(card.suit == "Diamonds" for card in player.card_list)):
# 		hand = "Flush"

# 	if set(card.value for card in player.card_list) in straights:
# 		if hand = "Flush":
# 			if "A" in set(card.value for card in player.card_list):
# 				hand = "Royal Flush"
# 			else:
# 				hand = "Straight Flush"
# 		else:
# 			hand = "Straight"
# 	elif:















