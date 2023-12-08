out = 0

with open("input.txt") as f:
	input = f.read()

lines = input.split('\n')

pattern = lines[0].strip()

graph = {}

for line in lines[1:]:
	if not line:
		continue

	start, end = line.strip().split(' = ')
	left, right = end.split(', ')

	graph[start] = [left[1:], right[:-1]]

node = "AAA"
pattern_idx = 0

while node != "ZZZ":
	left, right = graph[node]
	
	if pattern[pattern_idx] == "L":
		node = left
	else:
		node = right

	pattern_idx += 1
	pattern_idx %= len(pattern)

	out += 1
	

print(out)
