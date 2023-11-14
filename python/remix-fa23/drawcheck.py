import random

for _ in range(int(input())):
	s = [num for num in range(1, 501)]
	
	for _ in range(200):
		print('draw')
		
		l = list(map(int, input().split()))
		
		for i in l:
			if i in s:
				s.remove(i)
		
	for _ in range(49):
		n = random.choice(s)
		
		print(f'check {n}')
		
		if input() == "ABSENT":
			break
		
		s.remove(n)