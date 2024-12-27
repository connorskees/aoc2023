out = 0

with open("input.txt") as f:
	input = f.read()

matrix = [s.strip() for s in input.split('\n')]

height = len(matrix)
width = len(matrix[0])

digits = set('0123456789')

def check_adjacent(x, y):
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
			return True
		
	return False

for y in range(height):
	row = matrix[y]
	x = 0

	while x < width:
		while x < width and row[x] not in digits:
			x += 1
			continue

		found_symbol = False
		number = 0

		while x < width and row[x] in digits:
			number *= 10
			number += ord(row[x]) - ord('0')
			
			if not found_symbol and check_adjacent(x, y):
				found_symbol = True

			x += 1

		if found_symbol:
			out += number

print(out)
