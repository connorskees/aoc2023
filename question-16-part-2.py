out = 0

with open("input.txt") as f:
	input = f.read()

rows = input.split('\n')

height = len(rows)
width = len(rows[0])

left = (-1, 0)
right = (1, 0)
up = (0, -1)
down = (0, 1)

is_valid = lambda x, y: x >= 0 and y >= 0 and x < width and y < height

def attempt(x, y, dir):
	light_coords = set()

	visited = set()

	def traverse(x, y, dir):
		dir_x, dir_y = dir

		while is_valid(x, y):
			light_coords.add((x, y))

			if (x, y, dir) in visited:
				break

			visited.add((x, y, dir))

			c = rows[y][x]

			if c == '.':
				x, y = x + dir_x, y + dir_y
				continue

			if c == '-':
				if dir == up or dir == down:
					traverse(x, y, left)
					traverse(x, y, right)
					return
			elif c == '|':
				if dir == left or dir == right:
					traverse(x, y, up)
					traverse(x, y, down)
					return
			elif c == '/':
				if dir == left:
					dir = down
				elif dir == right:
					dir = up
				elif dir == up:
					dir = right
				else:
					dir = left
			elif c == '\\':
				if dir == left:
					dir = up
				elif dir == right:
					dir = down
				elif dir == up:
					dir = left
				else:
					dir = right
			
			dir_x, dir_y = dir
			x, y = x + dir_x, y + dir_y

	traverse(x, y, dir)

	return len(light_coords)

for x in range(width):
	out = max(out, attempt(x, 0, down))
	out = max(out, attempt(x, height-1, up))

for y in range(height):
	out = max(out, attempt(0, y, right))
	out = max(out, attempt(width-1, y, left))

print(out)
