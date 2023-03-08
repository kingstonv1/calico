from collections import deque


def looping_shift(number, shift):
	d = deque(number)
	d.rotate(shift)
	return int("".join(list(d)))


def solve(number):
	number = ([*number])
	permutations = list()
	
	for i in range(len(number)):
		permutations.append(looping_shift(number, i))

	return max(permutations)


for _ in range(int(input())):
	print(solve(input()))
	