from typing import List

def solve(S: str, R: int, C: int, P: List[List[str]]) -> None:
    '''
    Find the hidden word in the puzzle and output a copy of the puzzle with all
    letters except the letters of the hidden word replaced with #.
    
    S: the hidden word
    R: the number of rows in the puzzle
    C: the number of columns in the puzzlea
    P: the puzzle itself as a 2d list of characters
    '''
    rows = []
    row = int()
    ind = int()
    for i in range (R):
        row = str()
        
        for x in range (C):
            row += P[i][x]
        
        rows.append(row)
        
    for i in range (len(rows)):
        index = rows[i].find(S)
        if index != -1:
            row = i
            ind = index
    
    for r in range (R):
        if r != row:
            for c in range (C):
                P[r][c] = '#'
        
        else:
            try:
                for c in range (ind):
                    P[r][c] = '#'
                for c in range(C - (ind + len(S))):
                    P[r][C - c - 1] = '#' 
            except IndexError:
                print(ind)
                print(C)
                print(c)

    for x in range (R):
        for y in range (C):
            print(P[x][y], end = "")
        print()

def main():
    T = int(input())
    for _ in range(T):
        S = input()
        R, C = map(int, input().split(' '))
        P = [[c for c in input()] for _ in range(R)]
        # Don't forget the blank line in between test cases!
        input()
        solve(S, R, C, P)
        # Don't forget the blank line in between outputs!
        print()

if __name__ == '__main__':
    main()
