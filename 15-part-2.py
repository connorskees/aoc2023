from collections import defaultdict

out = 0

with open("input.txt") as f:
	input = f.read()

def hash(s):
	val = 0

	for c in s:
		val += ord(c)
		val *= 17
		val %= 256

	return val

boxes = defaultdict(lambda: {})

for s in input.strip().split(','):
	if '=' in s:
		s, num = s.split('=')
		boxes[hash(s)][s] = int(num)
	else:
		s = s[:-1]
		if s in boxes[hash(s)]:
			del boxes[hash(s)][s]

for box, slots in boxes.items():
	for idx, slot in enumerate(slots.values()):
		out += (box + 1) * (idx + 1) * slot

print(out)
