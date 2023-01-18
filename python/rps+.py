myMoves = []
botMoves = []
turn = 0


def beats(i):
    if i == "R":
        return "P"
    elif i == "P":
        return "S"
    elif i == "S":
        return "R"


def solve():
    if turn < 2:
        return "R"

    x = turn - 1

    if myMoves[x] == myMoves[x - 1]:
        return beats(beats(myMoves[x]))
    elif botMoves[x] == botMoves[x - 1]:
        return botMoves[x]
    else:
        return myMoves[x]

for _ in range(int(input())):
    m = solve()
    turn += 1
    myMoves.append(m)
    print(m)
    botMoves.append(input())