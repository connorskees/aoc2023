from collections import Counter

out = 0

hand_ordering = {
	"five": 6,
	"four": 5,
	"house": 4,
	"three": 3,
	"two pair": 2,
	"one pair": 1,
	"high": 0,
}

card_ordering = { c: -idx for idx, c in enumerate('AKQJT98765432') }

class Hand:
	def __init__(self, cards: str):
		counts = Counter(cards)

		max_run = max(counts.values())

		if max_run == 5:
			self.kind = "five"
		elif max_run == 4:
			self.kind = "four"
		elif max_run == 3:
			if min(counts.values()) == 2:
				self.kind = "house"
			else:
				self.kind = "three"
		elif max_run == 2:
			if len([v for v in counts.values() if v == 2]) > 1:
				self.kind = "two pair"
			else:
				self.kind = "one pair"
		else:
			self.kind = "high"

		self.cards = [card_ordering[c] for c in cards]
		self.orig_cards = cards

	def __str__(self):
		return self.orig_cards

	def __repr__(self):
		return f"{self}|{self.kind}"

	def __eq__(self, other):
		return self.orig_cards == other.orig_cards

	def __lt__(self, other):
		if hand_ordering[self.kind] == hand_ordering[other.kind]:
			return self.cards < other.cards
		
		return hand_ordering[self.kind] < hand_ordering[other.kind]

	def __gt__(self, other):
		if hand_ordering[self.kind] == hand_ordering[other.kind]:
			return self.cards > other.cards
		
		return hand_ordering[self.kind] > hand_ordering[other.kind]

with open("input.txt") as f:
	input = f.read()

hands = []

for hand in input.strip().split('\n'):
	cards, score = hand.strip().split()

	hands.append((Hand(cards), int(score)))

hands.sort(key=lambda n: n[0])

out = sum((idx + 1) * score for idx, (_, score) in enumerate(hands))

print(out)
