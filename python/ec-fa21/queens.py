def solve(board: list[str]) -> int:
    def is_safe(queens: list[tuple[int, int]], x, y) -> bool:
        for queen in queens:
            if queen[0] == x or queen[1] == y:
                return False
            
    return True
    
    
    # Scan the board for queens, putting them in a list
    queens = []
    
    for row in range(len(board)):
        for char in range(len(board[row])):
            if board[row][char] == 'Q':
                queens.append((row, char))
    
    return queens


def main():
    for _ in range(int(input())):
        rows = int(input()[0])
        board = []
        
        for _ in range(rows):
            board.append(input())
        
        print(solve(board))
        
        
main()
