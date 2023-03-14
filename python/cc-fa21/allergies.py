def solve(tests):
	negative = list()
	possible = list()
	known = list()
	
	# Filter out all negatives
	for i in tests:
		x = i.split()
		if x[1] == 'NEGATIVE':
			for allergen in x[2].split('/'):
				negative.append(allergen)
			tests.remove(i)
	
	for i in tests:
		tested = i.split()[2].split('/')
		pos = list(set(tested).difference(set(negative)))
		if len(pos) == 1:
			known.append(pos[0])
		else:
			for x in pos:
				possible.append(x)
	
	possible = list(set(possible).difference(set(known)))
	
	return f'KNOWN allergens: {"NONE" if len(known) == 0 else "/".join(set(known))}\n' \
		+ f'POTENTIAL allergens: {"None" if len(possible) == 0 else "/".join(set(possible))}'


for _ in range(int(input())):
	tests = list()
	numbers = input().split()
	n = int(numbers[0])
	m = int(numbers[1])
	
	allergens = input()
	
	for _ in range(n):
		tests.append(input())
	
	print(solve(tests))
	print()