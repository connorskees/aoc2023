out = 0

with open("input.txt") as f:
	input = f.read()

rows = input.split('\n')

height = len(rows)
width = len(rows[0])

light_coords = set()

left = (-1, 0)
right = (1, 0)
up = (0, -1)
down = (0, 1)

is_valid = lambda x, y: x >= 0 and y >= 0 and x < width and y < height

visited = set()

def traverse(x, y, dir):
	dir_x, dir_y = dir
	
	while is_valid(x, y):
		light_coords.add((x, y))

		if (x, y, dir) in visited:
			break

		visited.add((x, y, dir))

		x, y = x + dir_x, y + dir_y

		if not is_valid(x, y):
			break

		c = rows[y][x]

		if c == '.':
			continue

		if c == '-':
			if dir == up or dir == down:
				traverse(x, y, left)
				traverse(x, y, right)
				return
		elif c == '/':
			if dir == left:
				traverse(x, y, down)
			elif dir == right:
				traverse(x, y, up)
			elif dir == up:
				traverse(x, y, right)
			else:
				traverse(x, y, left)
			return
		elif c == '\\':
			if dir == left:
				traverse(x, y, up)
			elif dir == right:
				traverse(x, y, down)
			elif dir == up:
				traverse(x, y, left)
			else:
				traverse(x, y, right)
			return
		elif c == '|':
			if dir == left or dir == right:
				traverse(x, y, up)
				traverse(x, y, down)
				return

traverse(0, 0, down)

out = len(light_coords)

print(out)
