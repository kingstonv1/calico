from collections import defaultdict

def sort (numbers):
	length = len(numbers)
	
	for i in range(1, length):
		index = i
		
		while numbers[index] < numbers[index - 1] \
				and not (index - 1 < 0 or index == length):
			numbers[index - 1], numbers[index] = numbers[index], numbers[index - 1]
			index -= 1
	
	return numbers


def solve(students):
	pairs = defaultdict(lambda: 0)
	
	for i in range(len(students)):
		pairs[i + 1] = students[i]
	
	line = sort(list(pairs.values()))
	
	


for _ in range(int(input())):
	input()
	print(solve(list(map(int, input().split()))))