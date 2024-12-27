out = 1

with open("input.txt") as f:
	input = f.read()

lines = input.split('\n')

times = (int(n) for n in lines[0].strip().split(':')[-1].strip().split())
distances = (int(n) for n in lines[1].strip().split(':')[-1].strip().split())

races = ((t, d) for t, d in zip(times, distances))

for time, distance in races:
	num_ways = 0
	for t in range(time):
		speed = time - t
		if (time - speed) * speed > distance:
			num_ways += 1

	out *= num_ways

print(out)
