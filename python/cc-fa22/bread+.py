# Timelimit :(((((

def solve(n, d, menu):
	totals = list()
	
	for i in range(n):
		section = menu[i:i + d]
		
		if 0 in set(section):
			totals.append(sum(section[:section.index(0)]))
			continue

		totals.append(sum(section))
		
	return max(totals)


for _ in range(int(input())):
	inp = list(map(int, input().split()))
	m = list(map(int, input().split()))
	print(solve(inp[0], inp[2], m))
	