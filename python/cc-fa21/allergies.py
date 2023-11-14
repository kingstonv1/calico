def solve(allergens, tests):
	known = set()
	maybe = set()
	negative = set()
	
	n_tests = [t for t in tests if not t[0]]
	p_tests = [t for t in tests if t[0]]
	
	# First pass extracts negative results
	for test in n_tests:
		negative.update(test[1])
	
	# Second pass "cleans" the negatives out
	for test in p_tests:
		test[1].difference_update(negative)
	
	# Third pass sorts allergens into guaranteed positives and knowns
	for test in p_tests:
		if len(test[1]) == 1:
			known.update(test[1])
			continue

		maybe.update(test[1])

	maybe.difference_update(known)
	allergens.difference_update(negative.union(maybe.union(known)))
	maybe.update(allergens)
	
	known = list(known)
	maybe = list(maybe)
	known.sort()
	maybe.sort()
	
	print(f'KNOWN allergens: {"/".join(known) if known else "NONE"}')
	print(f'POTENTIAL allergens: {"/".join(maybe) if maybe else "NONE"}')
	print()
	

def main():
	for _ in range(int(input())):
		num_tests = int(input().split()[0])
		allergens = set(input().split())
		tests = []
		
		for _ in range(num_tests):
			i = input().split()
			
			# appends a tuple in the format(positive (True) or negative (False), test_string)
			tests.append([i[1] == "POSITIVE", set(i[2].split('/'))])
		
		solve(allergens, tests)
		
		input()
		

main()
