# Base Cases solved!
import random


def solve():
    n = random.randint(1, 3)
    if n == 1:
        return "R"
    elif n == 2:
        return "P"
    elif n == 3:
        return "S"


myMoves = []
botMoves = []
turn = 0

for _ in range(int(input())):
    print(solve())
    botMoves.append(input().strip())
