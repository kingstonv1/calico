def toWhite(p, Cow, Cbo, Cbw):
    if p == "brown":
        return min([Cbw, Cow + Cbo])
    elif p == "orange":
        return min([Cow, Cbo + Cbw])
    else:
        return
def toOrange(p, Cow, Cbo, Cbw):
    if p == "white":
        return min([Cow, Cbo + Cbw])
    elif p == "brown":
        return min([Cbo, Cow + Cbw])
    else:
        return
def toBrown(p, Cow, Cbo, Cbw):
    if p == "orange":
        return min([Cbo, Cow + Cbw])
    elif p == "white":
        return min([Cbw, Cow + Cbo])
    else:
        return

def solve(W: int, O: int, B: int, Cow: int, Cbo: int, Cbw: int) -> int:
    """
    Return the minimum cost to convert all of the paint into a single color.
    
    W: non-negative number of buckets of white paint
    O: non-negative number of buckets of orange paint
    B: non-negative number of buckets of brown paint
    Cow: positive cost to convert between a bucket of orange and white paint
    Cbo: positive cost to convert between a bucket of brown and orange paint
    Cbw: positive cost to convert between a bucket of brown and white paint
    """
    allWhite = 0
    allBrown = 0
    allOrange = 0
    
    allWhite += (toWhite("orange", Cow, Cbo, Cbw) * O)
    allWhite += (toWhite("brown", Cow, Cbo, Cbw) * B)
    
    allBrown += (toBrown("white", Cow, Cbo, Cbw) * W)
    allBrown += (toBrown("orange", Cow, Cbo, Cbw) * O)
    
    allOrange += (toOrange("white", Cow, Cbo, Cbw) * W)
    allOrange += (toOrange("brown", Cow, Cbo, Cbw) * B)
    
    return min([allWhite, allBrown , allOrange])


def main():
    T = int(input())
    for _ in range(T):
        line = input().split(' ')
        W, O, B = int(line[0]), int(line[1]), int(line[2])
        Cow, Cbo, Cbw = int(line[3]), int(line[4]), int(line[5])
        print(solve(W, O, B, Cow, Cbo, Cbw))

if __name__ == '__main__':
    main()
