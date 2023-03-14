import math



def extractPulseDistance(euclidean, pulse):
	return (euclidean - (math.dist((0, 0), (pulse[0], pulse[1])) * 2)) / 2


def sendPulse(x, y):
	print(f'P {x} {y}')
	euclideanDistance = float(input())
	return extractPulseDistance(euclideanDistance, (x, y))


def binarySearch(low, high, count, iterations, isX, defaultVal):
	lx, ly, hx, hy = defaultVal, defaultVal, defaultVal, defaultVal
	mid = (low + high) // 2
	
	if isX:
		lx = low
		hx = high
	else:
		ly = low
		hy = high
	
	l = sendPulse(lx, ly)
	h = sendPulse(hx, hy)
	
	count += 1
	
	if count == iterations:
		if l < h:
			return low
		else:
			return high
	else:
		if l < h:
			return binarySearch(low, mid, count, iterations, isX, defaultVal)
		else:
			return binarySearch(mid, high, count, iterations, isX, defaultVal)


def solve():
	steveX = binarySearch(-100000, 100000, 0, 18, isX = True, defaultVal = 0)
	steveY = binarySearch(-100000, 100000, 0, 18, isX = False, defaultVal = steveX)
	print(f'B {steveX} {steveY}')


for _ in range(int(input())):
	solve()
	input()
