from collections import defaultdict
import functools

out = 0

with open("input.txt") as f:
	input = f.read()

for line in input.split('\n'):
	gears, groups = line.split()

	gears = '?'.join([gears] * 5)
	groups = ','.join([groups] * 5)
	
	groups = [int(n) for n in groups.split(',')]
	gears = [g for g in gears.split('.') if g]

	@functools.cache
	def inner(gear_idx, group_idx):
		if group_idx >= len(groups) and gear_idx >= len(gears):
			return 1

		if gear_idx >= len(gears):
			return 0

		if group_idx >= len(groups):
			return int(all('#' not in g for g in gears[gear_idx:]))

		# fast path: if this group contains no ?, we can skip generating all
		# permutations
		if all(c == '#' for c in gears[gear_idx]):
			if len(gears[gear_idx]) != groups[group_idx]:
				return 0

			return inner(gear_idx + 1, group_idx + 1)

		valid_gears = { '': 1 }
		for c in gears[gear_idx]:
			if not valid_gears:
				return 0

			if c == '#':
				valid_gears = { gear + '#': count for gear, count in valid_gears.items() }
				continue

			v = defaultdict(int)

			for gear, count in valid_gears.items():
				if not gear:
					v[gear] += count
					v['#'] += count
					continue

				gear_groups = [g for g in gear.split('.') if g]

				if len(gear_groups) > len(groups) - group_idx:
					continue

				if len(gear_groups[-1]) > groups[group_idx + len(gear_groups) - 1]:
					continue

				if len(gear_groups) == len(groups) - group_idx and len(gear_groups[-1]) == groups[-1]:
					v[gear] += count
				elif gear[-1] == '#' and len(gear_groups[-1]) == groups[group_idx + len(gear_groups) - 1]:
					v[gear + '.'] += count
				else:
					if gear[-1] == '.':
						v[gear] += count
					v[gear + '#'] += count

			valid_gears = v

		total = 0

		# small optimization: above we can generate both groups `#` and `#.`.
		# deduplicate these groups to reduce recursion in some cases
		combined_gear_groups = defaultdict(int)
		for v, count in valid_gears.items():
			combined_gear_groups[v.strip('.')] += count

		for v, count in combined_gear_groups.items():
			v = [*(g for g in v.split('.') if g)]

			for idx, g in enumerate(v):
				if group_idx + idx >= len(groups) or len(g) != groups[group_idx + idx]:
					break
			else:
				total += inner(gear_idx + 1, group_idx + len(v)) * count

		return total
	
	out += inner(0, 0)

print(out)
