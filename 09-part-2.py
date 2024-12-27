out = 0

with open("input.txt") as f:
	input = f.read()

for line in input.split('\n'):
	nums = [int(n) for n in line.strip().split()]

	diffs = []

	while not all(n == 0 for n in nums):
		diffs.append(nums[0])
		for idx, num in enumerate(nums[:-1]):
			nums[idx] = nums[idx + 1] - num

		nums.pop()

	diff = 0

	for num in reversed(diffs):
		diff = num - diff

	out += diff

print(out)
