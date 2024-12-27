import math

out = 0

with open("input.txt") as f:
	input = f.read()

lines = input.split('\n')

pattern = lines[0].strip()

graph = {}
starts = []

for line in lines[1:]:
	if not line:
		continue

	start, end = line.strip().split(' = ')
	left, right = end.split(', ')

	if start[-1] == 'A':
		starts.append(start)

	graph[start] = [left[1:], right[:-1]]

def get_idx(start):
	node = start
	pattern_idx = 0

	while node[-1] != 'Z':
		left, right = graph[node]
		
		if pattern[pattern_idx % len(pattern)] == "L":
			node = left
		else:
			node = right

		pattern_idx += 1

	return pattern_idx

out = math.lcm(*(get_idx(s) for s in starts))

print(out)
