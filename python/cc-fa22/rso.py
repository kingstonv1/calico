def solve(Y, N):
    """
    Determine if the RSO name for an entry is valid. Return True if it is and
    return False otherwise.
    
    Y: the year the RSO was established
    N: the name the RSO registered with
    """
    split = N.split()
    x = split[0].upper()
    
    if Y > 2009:    
        if x == "CALIFORNIA" or x == "CAL" or x == "BERKELEY":
            return "INVALID"

    if len(N) > 50:
        return "INVALID"
    
    return "VALID"

def main():
    T = int(input())
    ans = []
    for _ in range(T):
        Y = int(input())
        N = input()
        ans.append(solve(Y, N))
            
    for i in (ans):
        print(i)

if __name__ == '__main__':
    main()
