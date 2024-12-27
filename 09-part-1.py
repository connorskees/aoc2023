out = 0

with open("input.txt") as f:
	input = f.read()

for line in input.split('\n'):
	nums = [int(n) for n in line.strip().split()]

	while not all(n == 0 for n in nums):
		out += nums[-1]
		for idx, num in enumerate(nums[:-1]):
			nums[idx] = nums[idx + 1] - num

		nums.pop()

print(out)
