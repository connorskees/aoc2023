from collections import defaultdict
import re

game = re.compile(r"Game (?P<id>\d+): (?P<games>(?:[^;]+(?:;|$))+)")
roll = re.compile(r"(?P<count>\d+) (?P<color>blue|red|green)")

out = 0

with open("input.txt") as f:
	input = f.read()

for line in input.split('\n'):
	groups = re.match(game, line.strip())

	id = int(groups.group("id"))
	games = groups.group("games")

	rolls = defaultdict(int)
	for g in games.split(";"):
		for r in g.split(','):
			for r in re.finditer(roll, r.strip()):
				rolls[r.group("color")] = max(int(r.group("count")), rolls[r.group("color")])
	out += rolls["red"] * rolls["green"] * rolls["blue"]

print(out)
