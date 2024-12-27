out = 0

with open("input.txt") as f:
	input = f.read()

rows = input.split('\n')

height = len(rows)
width = len(rows[0])

empty_rows = []
empty_cols = []

for x in range(width):
	if all(row[x] == '.' for row in rows):
		empty_cols.append(x)

for y in range(height):
	if all(c == '.' for c in rows[y]):
		empty_rows.append(y)

galaxies = []

for y in range(height):
	for x in range(width):
		if rows[y][x] == '#':
			galaxies.append((x, y))

manhattan = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

adjust = lambda x, y: (x + len([c for c in empty_cols if c <= x]), y + len([c for c in empty_rows if c <= y]))

for i in range(len(galaxies)):
	for j in range(i+1, len(galaxies)):
		a = adjust(*galaxies[i])
		b = adjust(*galaxies[j])

		out += manhattan(a, b)

print(out)
