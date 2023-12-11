from collections import deque
from typing import Set

class Line:
	def __init__(self, x1: int, y1: int, x2: int, y2: int):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def __repr__(self):
		return f'[({self.x1}, {self.y1}), ({self.x2}, {self.y2})]'
	
	def __eq__(self, other):
		return [self.x1, self.y1, self.x2, self.y2] == [other.x1, other.y1, other.x2, other.y2]
	
	def __hash__(self):
		return hash((self.x1, self.y1, self.x2, self.y2))

	def intersects(self, other: 'Line') -> bool:
		# https://stackoverflow.com/a/9997374
		def ccw(A,B,C):
			return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

		# Return true if line segments AB and CD intersect
		def intersect(A,B,C,D):
			return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

		return intersect((self.x1, self.y1), (self.x2, self.y2), (other.x1, other.y1), (other.x2, other.y2))

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

start_x, start_y = start
rows[start_y] = rows[start_y][:start_x] + start_char + rows[start_y][start_x+1:]

queue = deque([(*start, 0, start_char, start)])

visited = set([start])

lines: Set[Line] = set()

last = deque()

# traverse the graph once to find the main loop and represent it as a series of
# line segments

while queue:
	x, y, length, char, line_start = queue.popleft()

	visited.add((x, y))

	can_travel = directions_travelled[char]

	for x2, y2, mask in masks_and_dirs(x, y):
		if (x2, y2) in visited or not is_valid(x2, y2):
			continue

		if can_travel & mask & directions_accepted[rows[y2][x2]]:
			this_line_start = line_start
			if rows[y2][x2] in 'L7FJ':
				lines.add(Line(*line_start, x2, y2))
				this_line_start = (x2, y2)
				last.append(this_line_start)

				if len(last) > 2:
					last.popleft()

			queue.append((x2, y2, length+1, rows[y2][x2], this_line_start))

lines.add(Line(*last[0], *last[1]))

# identify enclosed coords using even-odd rule

for y in range(1, height - 1):
	for x in range(1, width - 1):
		if (x, y) in visited:
			continue

		ray = Line(x, y, x+500, y+500)

		num_hit = 0

		for line in lines:
			if line.intersects(ray):
				num_hit += 1

		if num_hit % 2 == 1:
			out += 1

print(out)
