def solve(students: list[int]):
	s = {}
	wait, temp = 0, 0
	
	for i in range(1, len(students) + 1):
		s[i] = students[i - 1]
	
	srted = {k: v for k, v in sorted(s.items(), key = lambda item: item[1])}
	
	for i in srted.values():
		temp += i
		wait += temp
	
	return srted.keys()


def main():
	for _ in range(int(input())):
		input()
		students = list(map(int, input().split()))
		print(*solve(students))
		
		
main()
