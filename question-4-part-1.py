out = 0

with open("input.txt") as f:
	input = f.read()

for line in input.split('\n'):
	_, numbers = line.strip().split(':')
	winning, have = numbers.strip().split('|')
	
	winning = { s for s in winning.split(' ') if s }
	have = { s for s in have.split(' ') if s }

	overlap = len(winning & have)

	if overlap == 0:
		continue

	out += 2 ** (overlap - 1)

print(out)
