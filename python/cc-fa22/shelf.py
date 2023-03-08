def solve(N, B, W, D, H):
    """
    Find the total volume of wood needed to construct the given bookshelf design.

    N: the number of shelves in the bookshelf
    B: the thickness of the boards, in inches
    W: the width of the shelves, in inches
    D: the depth of the bookshelf, in inches
    H: the list of integers denoting the height of each of the bookshelf’s shelves, in inches
    """
    s = sum(H)
    height = s + (B  * (N + 1))
    sideBoard = B * height * D
    board = B * W * D
    topBoard = B * W * D
    
    return ((sideBoard * 2) + (topBoard) + (board * N))

def main():
    T = int(input())
    sol = []
    for _ in range(T):
        N, B, W, D = (int(i) for i in input().split())
        H = [int(x) for x in input().strip().split(' ')]
        sol.append(solve(N, B, W, D, H))
    
    for i in sol:
        print(i)

if __name__ == '__main__':
    main()
    
