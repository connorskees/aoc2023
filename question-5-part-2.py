import math

out = math.inf

with open("input.txt") as f:
	input = f.read()

lines = input.split('\n')

seeds = lines[0].split(':')[-1].strip().split(' ')

starts = seeds[::2]
lengths = seeds[1::2]

seed_intervals = [(int(start), int(start)+int(length) - 1) for start, length in zip(starts, lengths)]

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

		intervals.append((int(source_start), int(source_start) + int(length)  - 1, int(dest_start)))

		idx += 1

	maps.append(intervals)

	idx += 1

next_intervals = []

for map in maps:
	while seed_intervals:
		seed_start, seed_end = seed_intervals.pop()

		for source_start, source_end, dest_offset in map:
			if seed_start >= source_start and seed_start <= source_end:
				if seed_end > source_end:
					seed_intervals.append((source_end + 1, seed_end))
					seed_end = source_end			

				seed_interval_length = seed_end - seed_start

				next_start = seed_start - source_start + dest_offset
				next_end = next_start + seed_interval_length
				next_intervals.append((next_start, next_end))
				break
		else:
			next_intervals.append((seed_start, seed_end))

	seed_intervals = next_intervals
	next_intervals = []

out = min(s[0] for s in seed_intervals)

print(out)
