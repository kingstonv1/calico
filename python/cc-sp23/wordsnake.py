def solve(word, puz):
	invalid = set()
	
	def rsearch(x, y, idx, visited):
		pass
		
	
				

	res = None

	for i in range(len(puz[0])):
		for e in range(len(puz)):
			if puz[i][e] != word[0]:
				continue
			
			res = rsearch(i, e, 1, [])
			
			if res:
				break

	for i in range(len(puz[0])):
		for e in range(len(puz)):
			if puz[i][e] not in res:
				puz[i][e] = '#'

	return "\n".join(["".join(line) for line in puz])


def main():
	for _ in range(int(input())):
		word = input()
		cols = int(input()[0])
		puz = list()

		for _ in range(cols):
			puz.append(list(input()))
			
		print(solve(word, puz))
	
	
main()
