def solve(towers):
    # bruteforce approach
    m = float('inf')

    for i in range(len(towers)):
        power = 0
        
        for x in range(len(towers)):
            this_power = towers[(i + x) % len(towers)][0]
            this_path = towers[(i + x) % len(towers)][1]
            
            # if we need to wait in the tower
            if this_power > power:
                power += this_power - power
            
            # do not take the last path in the cycle
            if x != len(towers) - 1:
                power += this_path
            
        m = min(power, m)

    return m

def main():
    for _ in range(int(input())):
        n = int(input())
        powers = list(map(int, input().split()))
        paths = list(map(int, input().split()))
        
        l = [(powers[i], paths[i]) for i in range(n)]
        
        print(solve(l))


main()
