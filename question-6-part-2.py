out = 0

with open("input.txt") as f:
	input = f.read()

lines = input.split('\n')

time = int(lines[0].strip().split(':')[-1].strip().replace(" ", ""))
distance = int(lines[1].strip().split(':')[-1].strip().replace(" ", ""))

start = None
end = None

### you can also do the below using binary search, but this finishes for the
### given input in under 5 seconds

for t in range(time):
	speed = time - t
	if (time - speed) * speed > distance:
		start = t
		break

for t in reversed(range(time)):
	speed = time - t
	if (time - speed) * speed > distance:
		end = t
		break

out = end - start + 1

print(out)
