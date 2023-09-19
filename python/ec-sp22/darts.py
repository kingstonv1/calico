def solve(boardSize: int, counter: int, board: list[str]):
	line = ""
	center = int(boardSize / 2)
	spaces = int(counter / 2 + 0.5)
	
	line += "X " * spaces
	
	if counter % 2 == 0:
		line += "X" * (boardSize - counter * 2) + " "
	else:
		line += " " * ((boardSize - counter * 2) - 1)
		
	line += "X " * spaces
	
	board.append(line)
	
	if counter == center:
		board += list(reversed(board[:-1]))
		return board
		
	return solve(boardSize, counter + 1, board)
		

for _ in range(int(input())):
	print("\n".join(solve(int(input()) * 2 - 1, 0, [])))
	