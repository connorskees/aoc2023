out = 0

with open("input.txt") as f:
	input = f.read()

rows = [list(r) for r in input.split('\n')]

height = len(rows)
width = len(rows[0])

def move_north():
	idxs = [0] * width

	for y in range(height):
		for x in range(width):
			if rows[y][x] == '#':
				idxs[x] = y + 1
			elif rows[y][x] == 'O':
				rows[y][x], rows[idxs[x]][x] = rows[idxs[x]][x], rows[y][x]
				idxs[x] += 1

def move_right():
	for y in range(height):
		last_seen = width - 1

		for x in reversed(range(width)):
			if rows[y][x] == '#':
				last_seen = x - 1
				continue


			if rows[y][x] == 'O':
				rows[y][x], rows[y][last_seen] = rows[y][last_seen], rows[y][x]
				last_seen -= 1

def move_left():
	for y in range(height):
		last_seen = 0

		for x in range(width):
			if rows[y][x] == '#':
				last_seen = x + 1
				continue

			if rows[y][x] == 'O':
				rows[y][x], rows[y][last_seen] = rows[y][last_seen], rows[y][x]
				last_seen += 1

def move_south():
	idxs = [height - 1] * width
	
	for y in reversed(range(height)):
		for x in range(width):
			if rows[y][x] == '#':
				idxs[x] = y - 1
			elif rows[y][x] == 'O':
				rows[y][x], rows[idxs[x]][x] = rows[idxs[x]][x], rows[y][x]
				idxs[x] -= 1

def compute_load():
	return sum(height - y for x in range(width) for y in range(height) if rows[y][x] == 'O')
	
seen = {''.join((''.join(r) for r in rows)): -1 }

cycle_length = -1
cycle_offset = -1

i = 0
while True:
	move_north()
	move_left()
	move_south()
	move_right()

	joined = ''.join((''.join(r) for r in rows))

	if joined in seen:
		cycle_length = i - seen[joined]
		cycle_offset = seen[joined]
		break

	seen[joined] = i

	i += 1

remaining = (1_000_000_000 - cycle_offset) % cycle_length - 1

for _ in range(remaining):
	move_north()
	move_left()
	move_south()
	move_right()

out = compute_load()

print(out)
