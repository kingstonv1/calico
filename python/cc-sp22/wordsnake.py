# this approach definitely doesn't work lol

goodLetters = list()
badLetters = set()


def reveal(puzzle):
	global goodLetters
	goodLetters = set(goodLetters)
	
	for row in range(len(puzzle)):
		for col in range(len(puzzle[row])):
			if (row, col) not in goodLetters:
				puzzle[row][col] = '#'
				
	for row in range(len(puzzle)):
		puzzle[row] = str(puzzle[row])
	
	return puzzle


def search_for_letter(letter, puzzle):
	global badLetters
	
	for row in range(len(puzzle)):
		for col in range(len(puzzle[row])):
			if puzzle[row][col] == letter and puzzle[row][col] not in badLetters:
				return row, col


def solve(word, rows, cols, puzzle, position):
	if not goodLetters:
		position = search_for_letter(word[0], puzzle)
		
		
for _ in range(int(input())):
	hidden = input()
	rowcol = list(map(int, input().split()))
	grid = [list(input()) for _ in range(rowcol[0])]
	solved = solve(hidden, rowcol[0], rowcol[1], grid, (0, 0))
	for r in solved:
		print(r)
	input()
	