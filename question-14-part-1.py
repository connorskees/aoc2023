import heapq

out = 0

with open("input.txt") as f:
	input = f.read()

rows = input.split('\n')

height = len(rows)
width = len(rows[0])

boulders_by_col = []

for x in range(width):
	boulders = [y for y in range(height) if rows[y][x] == '#']
	heapq.heapify(boulders)
	boulders_by_col.append(boulders)

for y, row in enumerate(rows):
	for x, col in enumerate(row):
		if col != 'O':
			continue

		can_slide_to = 0

		h = boulders_by_col[x]

		while h:
			if h[0] > y:
				break
			
			n = heapq.heappop(h)

			can_slide_to = n + 1

		out += height - can_slide_to

		heapq.heappush(h, can_slide_to)

print(out)
