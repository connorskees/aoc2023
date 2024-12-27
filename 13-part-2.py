def lines_equal_minus_one(a, b):
	if a == b:
		return (True, False)

	skipped = False

	for idx in range(len(a)):
		if a[idx] == b[idx]:
			continue

		if skipped:
			return (False, False)
		
		skipped = True

	return (True, skipped)

out = 0

with open("input.txt") as f:
	input = f.read()

grids = input.split('\n\n')

def get_flip(grid: str, can_skip: bool):
	"""returns (row, col)"""
	lines = grid.split('\n')
	row = None
	possible_cols = { n: False for n in range(len(lines[0]) - 1) }
	
	for idx, line in enumerate(lines):
		start_row = idx
		end_row = idx + 1

		skipped = not can_skip

		flipped_horizontally = idx != len(lines) - 1 and lines_equal_minus_one(line, lines[idx+1])

		while start_row >= 0 and end_row < len(lines):
			equal, had_to_skip = lines_equal_minus_one(lines[start_row], lines[end_row])
			if not equal or (had_to_skip and skipped):
				flipped_horizontally = False
				break

			skipped = skipped or had_to_skip

			start_row -= 1
			end_row += 1

		if flipped_horizontally and skipped:
			row = idx

		for idx in [*possible_cols.keys()]:
			start_col = idx
			end_col = idx + 1

			skipped = not can_skip

			while start_col >= 0 and end_col < len(line):
				if line[start_col] != line[end_col]:
					if skipped:
						del possible_cols[idx]
						break

					skipped = True

				start_col -= 1
				end_col += 1

			if idx in possible_cols and skipped and can_skip:
				if possible_cols[idx]:
					del possible_cols[idx]
				else:
					possible_cols[idx] = True

	if possible_cols:
		possible_cols = [k for k, v in possible_cols.items() if (v and can_skip) or not can_skip]
		assert not possible_cols or len(possible_cols) == 1, f"{possible_cols}"

	return (row, possible_cols[0] if possible_cols else None)

for grid in grids:
	row, col = get_flip(grid, True)

	if row is None:
		out += col + 1
	else:
		out += 100 * (row + 1)

print(out)
