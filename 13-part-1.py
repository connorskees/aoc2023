out = 0

with open("input.txt") as f:
    input = f.read()

grids = input.split("\n\n")

for grid in grids:
    lines = grid.split("\n")
    row = None
    possible_cols = set(range(len(lines[0]) - 1))

    for idx, line in enumerate(lines):
        start_row = idx
        end_row = idx + 1

        flipped_horizontally = idx != len(lines) - 1 and line == lines[idx + 1]

        while start_row >= 0 and end_row < len(lines):
            if lines[start_row] != lines[end_row]:
                flipped_horizontally = False
                break

            start_row -= 1
            end_row += 1

        if flipped_horizontally:
            row = idx
            break

        flipped_vertically = False

        for idx in [*possible_cols]:
            start_col = idx
            end_col = idx + 1

            while start_col >= 0 and end_col < len(line):
                if line[start_col] != line[end_col]:
                    possible_cols.remove(idx)
                    break

                start_col -= 1
                end_col += 1

    if row is None:
        out += list(possible_cols)[0] + 1
    else:
        out += 100 * (row + 1)

print(out)
