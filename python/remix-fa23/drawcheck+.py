import random

for _ in range(int(input())):
	s = {i for i in range(1, 501)}
	
	counter = 0
	while (len(s) > (90 - counter)) and counter < 70:
		print('draw')
		for num in map(int, input().split()):
			s.discard(num)
		counter += 1
	
	s = list(s)
	random.shuffle(s)
	
	for num in s:
		print(f'check {num}')
		
		if input() == 'ABSENT':
			break