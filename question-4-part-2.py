from collections import defaultdict

out = 0

with open("input.txt") as f:
	input = f.read()

scratchcards = defaultdict(int)

for line in input.split('\n'):
	id, numbers = line.strip().split(':')

	id = int(id.strip().split(' ')[-1])

	winning, have = numbers.strip().split('|')
	
	winning = { s for s in winning.split(' ') if s }
	have = { s for s in have.split(' ') if s }

	overlap = len(winning & have)

	if overlap == 0:
		continue

	count = scratchcards[id] + 1

	for i in range(id+1, id+overlap+1):
		scratchcards[i] += count

out = sum(scratchcards.values())  + len(input.split('\n'))

print(out)
