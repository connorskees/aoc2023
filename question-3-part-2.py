from collections import defaultdict

out = 0

with open("input.txt") as f:
	input = f.read()

matrix = [s.strip() for s in input.split('\n')]

height = len(matrix)
width = len(matrix[0])

digits = set('0123456789')

def check_adjacent(x, y):
	gear_coords = set()
	adjacent = [
		(x+1, y),
		(x, y+1),
		(x+1, y+1),
		(x-1, y),
		(x, y-1),
		(x-1, y-1),
		(x+1, y-1),
		(x-1, y+1),
	]

	for x, y in adjacent:
		if x < 0 or y < 0 or x >= width or y >= height:
			continue

		if matrix[y][x] not in digits and matrix[y][x] != '.':
			gear_coords.add((x, y))
		
	return gear_coords

gears = defaultdict(list)

for y in range(height):
	row = matrix[y]
	x = 0

	while x < width:
		while x < width and row[x] not in digits:
			x += 1
			continue

		gear_coords = set()
		number = 0

		while x < width and row[x] in digits:
			number *= 10
			number += ord(row[x]) - ord('0')
			
			gear_coords.update(check_adjacent(x, y))

			x += 1
		
		if number == 0:
			continue

		for coords in gear_coords:
			gears[coords].append(number)

out = sum(g[0] * g[1] for g in gears.values() if len(g) == 2)

print(out)
