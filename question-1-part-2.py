class TrieNode:
	def __init__(self, c: str) -> None:
		self.c = c
		self.children = {}
		self.is_word_end = False

class Trie:
	def __init__(self) -> None:
		self.root = TrieNode("")

	def insert(self, s: str):
		node = self.root

		for c in s:
			if c not in node.children:
				node.children[c] = TrieNode(c)
			node = node.children[c]

		node.is_word_end = True

out = 0

with open("input.txt") as f:
	input = f.read()

numbers = {
	"zero": 0,
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
	**{ str(n): n for n in range(10) },
}

trie = Trie()

for n in numbers.keys():
	trie.insert(n)

for line in input.split('\n'):
	if not line:
		continue

	first = None
	last = None

	for idx, c in enumerate(line):
		node = trie.root

		if c not in node.children:
			continue

		word = ""

		while c in node.children and not node.is_word_end:
			word += c
			node = node.children[c]
			idx += 1
			if idx >= len(line):
				break
			c = line[idx]

		if not node.is_word_end:
			continue
		
		if first is None:
			first = numbers[word]
		last = numbers[word]

	out += first * 10 + last	

print(out)
