t = int(input())

import time

def queenMoves(a, x, y):
    a[x][y] = 'X' # You cannot capture queens.
    
    # Up Left
    for i in range (1000000):
        try:
            if x - i >= 0 and y - i >= 0:
                a[x - i][y - i] = 'X'
        except IndexError:
            print("Broken. Index hit " + str(i))
            break
    # Up
    for i in range (1000000):
        try:
            if y - i >= 0:
                a[x][y - i] = 'X'
        except IndexError:
            print("Broken. Index hit " + str(i))
            break
    # Up Right
    for i in range (1000000):
        try:
            if y - i >= 0:
                a[x + i][y - i] = 'X'
        except IndexError:
            print("Broken. Index hit " + str(i))
            break
    # Right
    for i in range (1000000):
        try:
            a[x + i][y] = 'X'
        except IndexError:
            print("Broken. Index hit " + str(i))
            break
    # Down Right
    for i in range (1000000):
        try:
            a[x + i][y + i] = 'X'
        except IndexError:
            print("Broken. Index hit " + str(i))
            break
    # Down
    for i in range (1000000):
        try:
            a[x][y + i] = 'X'
        except IndexError:
            print("Broken. Index hit " + str(i))
            break
    # Down Left
    for i in range (1000000):
        try:
            if x - i >= 0:
                a[x - i][y + i] = 'X'
        except IndexError:
            print("Broken. Index hit " + str(i))
            break
    # Left
    for i in range (1000000):
        try:
            if x - i >= 0:
                a[x - i][y] = 'X'
        except IndexError:
            print("Broken. Index hit " + str(i))
            break
    
    return a

def isMate(a, x, y, xm, ym):
    xSubAllow = x - 1 >= 0
    ySubAllow = y - 1 >= 0
    xAddAllow = x + 1 < xm
    yAddAllow = y + 1 < ym
    
    if xSubAllow and ySubAllow:
        if not a[x - 1][y - 1] == 'X':
            return False
    if xSubAllow:
        if not a[x - 1][y] == 'X':
            return False
    if xSubAllow and yAddAllow:
        if not a[x - 1][y + 1] == 'X':
            return False
    if ySubAllow:
        if not a[x][y - 1] == 'X':
            return False
    if xAddAllow and ySubAllow:
        if not a[x + 1][y - 1] == 'X':
            return False
    if xAddAllow:
        if not a[x + 1][y] == 'X':
            return False
    if yAddAllow:
        if not a[x][y + 1] == 'X':
            return False
    if xAddAllow and yAddAllow:
        if not a[x + 1][y + 1] == 'X':
            return False
    
    if not a[x][y] == 'X':
        return False
    
    return True


counts = []

for q in range (t):
    count = 0
    
    boardIn = []
    
    dims = input()
    
    dimX = int(dims[0])
    dimY = int(dims[2])
    
    for w in range (dimX):
        boardIn.append(input())
    
    start = time.time()
    
        
    board = [['' for i in range(dimY)] for j in range (dimX)]
    attacks = [['' for i in range(dimY)] for j in range (dimX)]
    
    # Parse the chess board into a 2d array
    for i in range (dimX):
        for x in range (dimY):
            board[i][x] = boardIn[i][x]
    
    for i in range (dimX):
        for x in range (dimY):
            if board[i][x] == 'Q':
                attacks = queenMoves(attacks, i, x)
    
    for i in range (dimX):
        for x in range (dimY):
            if board[i][x] != 'Q':
                if isMate(attacks, i, x, dimX, dimY):
                    count += 1
    
    counts.append(count)
    end = time.time()
    print("The time to complete the calculations: " + str(end - start))
    input()

for num in counts:
    print(num)