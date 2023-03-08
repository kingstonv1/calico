def solve(age1, age2, name1, name2):
	greater = max((age1, age2))
	lesser = min((age1, age2))
	
	if age1 > age2:
		greatestFirst = True
	else:
		greatestFirst = False
	
	greaterFinal = (greater - lesser) * 2
	lesserFinal = greaterFinal // 2
	
	if lesserFinal >= lesser:
		if greatestFirst:
			return f'In {lesserFinal - lesser} year(s):\n{name1} will be {greaterFinal} and {name2} will be {lesserFinal}'
		else:
			return f'In {lesserFinal - lesser} year(s):\n{name1} will be {lesserFinal} and {name2} will be {greaterFinal}'
	
	return "Time will end before you are happy"


for _ in range(int(input())):
	i = input().split()
	print(solve(int(i[1]), int(i[3]), i[0], i[2]))
	print()