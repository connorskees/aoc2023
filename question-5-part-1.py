import math

out = math.inf

with open("input.txt") as f:
	input = f.read()

lines = input.split('\n')

seeds = lines[0].split(':')[-1].strip().split(' ')

maps = []

idx = 2

while idx < len(lines):
	line = lines[idx]
	name, _ = line.split(' ')

	intervals = []

	idx += 1

	while idx < len(lines) and lines[idx].strip():
		line = lines[idx]

		dest_start, source_start, length = line.strip().split(' ')

		intervals.append((int(source_start), int(source_start) + int(length), int(dest_start)))

		idx += 1

	maps.append(intervals)

	idx += 1

for seed in seeds[1:]:
	seed = int(seed)

	for map in maps:
		for start, end, dest_offset in map:
			if seed >= start and seed <= end:
				seed = seed - start + dest_offset
				break

	out = min(out, seed)
	

print(out)
