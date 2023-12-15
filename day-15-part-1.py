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

for s in input.strip().split(','):
	out += hash(s)

print(out)
