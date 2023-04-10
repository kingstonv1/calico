from collections import defaultdict

def solve(diceFaces, totalFaces):
	# Edge case where there are no duplicate faces - return the largest number.
	if list(set(diceFaces)) == diceFaces:
		return max(diceFaces)
	
	# Initalize a dict where keys carry a value of 0 by default.
	occurrenceCounter = defaultdict(lambda: 0)
	
	for i in diceFaces:
		occurrenceCounter[i] += 1
		
	# Determine the 'value' of zeroing a number by its probability * its numerical avlue
	faceValues = dict()
	
	for i in occurrenceCounter.keys():
		faceValues[i] = (occurrenceCounter[i] / totalFaces) * i
	
	return max(faceValues, key = faceValues.get)


for _ in range(int(input())):
	numFaces = int(input())
	faces = list(map(int, input().split()))
	
	print(solve(faces, numFaces))
	