from collections import deque

out = 0

with open("input.txt") as f:
	input = f.read()

rows = input.split('\n')

height = len(rows)
width = len(rows[0])

start_idx = input.index('S')

start = (start_idx % (width + 1), start_idx // (width + 1))

left = 0b0001
right = 0b0010
up = 0b0100
down = 0b1000

directions_accepted = {
	'|': up | down,
	'-': left | right,
	'L': down | left,
	'J': down | right,
	'7': up | right,
	'F': up | left,
	'.': 0,
	'S': 0,
}

directions_travelled = {
	'|': up | down,
	'-': left | right,
	'L': up | right,
	'J': up | left,
	'7': down | left,
	'F': down | right,
	'.': 0,
	'S': 0,
}

is_valid = lambda x, y: x >= 0 and y >= 0 and x < width and y < height
masks_and_dirs = lambda x, y: [(x-1, y, left), (x+1, y, right), (x, y-1, up), (x, y+1, down)]

possible_start_dirs = 0

for x, y, mask in masks_and_dirs(*start):
	possible_start_dirs |= directions_accepted[rows[y][x]] & mask

start_char = next(c for c, d in directions_travelled.items() if possible_start_dirs == d)

queue = deque([(*start, 0, start_char)])

visited = set([start])

while queue:
	x, y, length, char = queue.popleft()

	out = max(out, length)

	visited.add((x, y))

	can_travel = directions_travelled[char]

	for x2, y2, mask in masks_and_dirs(x, y):
		if (x2, y2) in visited or not is_valid(x2, y2):
			continue

		if can_travel & mask:
			queue.append((x2, y2, length+1, rows[y2][x2]))

print(out)
