digits = set('0123456789')

out = 0

with open("input.txt") as f:
	input = f.read()

for line in input.split('\n'):
	if not line:
		continue

	first = None
	last = None
	for c in line:
		if c not in digits:
			continue
		if first is None:
			first = c
		last = c

	out += ord(last) - ord('0')
	out += 10 * (ord(first) - ord('0'))

print(out)
