import copy


def printArray(a):
	for row in a:
		for col in row:
			print(col, end="")
		print("")


def solve(width, depth, prism):
	# Record the original face for later use
	"""copy.deepcopy was the only thing I tried that worked as a copy instead of a reference.
	hopefully it's not too slow :("""
	face = copy.deepcopy(prism)
	
	# Index the location of the '+' characters before adding space, to save time
	edges = list()
	
	for col in range(len(prism)):
		for row in range(len(prism[col])):
			if prism[row][col] != "+":
				continue
			edges.append([row, col])
	
	# Add space for extrusion - the max additional space you'll need is the same as the depth + 1.
	# Add horizontal space
	for row in prism:
		for _ in range(depth + 2):
			row.append(" ")
	# Add vertical space
	for _ in range(depth + 2):
		prism.append([" " for _ in range(width + depth + 1)])
	
	# Take a greedy approach, extruding each '+' character that you see from left to right.
	for edge in edges:
		x = edge[0]
		y = edge[1]
		
		if prism[x][y] != '+':
			for i in range(1, depth + 1):
				if prism[x + i][y + i] == " ":
					prism[x + i][y + i] = '\\'
		
		for i in range(1, depth + 1):
			prism[x + i][y + i] = '\\'
			
	# Finally, place the original shape at the front of our perspective.
	offset = depth + 1

	for h in range(len(face)):
		for w in range(len(face[h])):
			prism[w + offset][h + offset] = face[w][h]
			
	return prism
	
	
for _ in range(int(input())):
	hwd = list(map(int, input().split()))
	height = hwd[0]
	width = hwd[1]
	depth = hwd[2]
	
	shape = list()
	
	for i in range(height):
		shape.append(list(input()))
	
	printArray(solve(width, depth, shape))
	