import math
from typing import Tuple
import heapq

out = math.inf

with open("input.txt") as f:
	input = f.read()

rows = input.split('\n')

left = (-1, 0)
right = (1, 0)
up = (0, -1)
down = (0, 1)

height = len(rows)
width = len(rows[0])

class TraversalState:
	def __init__(
		self,
		x: int,
		y: int,
		dir: Tuple[int, int],
		run_length: int,
		cost: int,
	) -> None:
		self.x = x
		self.y = y
		self.dir = dir
		self.run_length = run_length
		self.cost = cost

	def is_valid(self):
		return self.x >= 0 and self.y >= 0 and self.x < width and self.y < height

	def _computed_cost(self):
		return self.cost + int(rows[self.y][self.x])
	
	def __lt__(self, other):
		return self._computed_cost() < other._computed_cost()
	
	def _hash_key(self):
		return (self.x, self.y, self.dir, self.run_length)

	def __eq__(self, other):
		return self._hash_key() == other._hash_key()
	
	def __hash__(self):
		return hash(self._hash_key())
	
	def __gt__(self, other):
		return self._computed_cost() > other._computed_cost()

	def __repr__(self):
		dir_names = {
			left: "left",
			right: "right",
			up: "up",
			down: "down",
		}
		d = dir_names[self.dir]
		return f"({self.x}, {self.y}, ({self.run_length}, {d})); cost: {self._computed_cost()}, {rows[self.y][self.x]}"

queue = [TraversalState(1, 0, right, 1, 0), TraversalState(0, 1, down, 1, 0)]

heapq.heapify(queue)

possible_dirs = {
	left: [up, down],
	right: [up, down],
	up: [left, right],
	down: [left, right],
}

visited = set()

while queue:
	state = heapq.heappop(queue)

	if not state.is_valid() or state in visited:
		continue

	if state.x == width - 1 and state.y == height - 1 and state.run_length >= 4:
		out = min(out, state._computed_cost())
		break

	visited.add(state)

	cost = state._computed_cost()

	dirs = []

	if state.run_length >= 4:
		dirs += possible_dirs[state.dir]

	if state.run_length < 10:
		dirs.append(state.dir)

	for dir in dirs:
		n = TraversalState(
			state.x + dir[0],
			state.y + dir[1],
			dir,
			1 if dir != state.dir else state.run_length + 1,
			cost,
		)

		if not n.is_valid() or n in visited:
			continue

		heapq.heappush(queue, n)

print(out)
