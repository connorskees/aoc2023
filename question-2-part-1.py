from collections import defaultdict
import re

game = re.compile(r"Game (?P<id>\d+): (?P<games>(?:[^;]+(?:;|$))+)")
roll = re.compile(r"(?P<count>\d+) (?P<color>blue|red|green)")

out = 0

red = 12
green = 13
blue = 14
total = red + blue + green

with open("input.txt") as f:
	input = f.read()

for line in input.split('\n'):
	groups = re.match(game, line.strip())

	id = int(groups.group("id"))
	games = groups.group("games")

	for g in games.split(";"):
		rolls = defaultdict(int)
		for r in g.split(','):
			for r in re.finditer(roll, r.strip()):
				rolls[r.group("color")] = int(r.group("count"))

		if sum(rolls.values()) > total:
			break

		if rolls["red"] > red or rolls["green"] > green or rolls["blue"] > blue:
			break
	else:
		out += id

print(out)
