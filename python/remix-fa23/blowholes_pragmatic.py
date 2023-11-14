# this was a really good idea but ultimately flawed. idk how but it fails like 25 tcs lol

def x(whales, k):
    groups = [[]]
    cur_floor = whales[0]
    idx = 0
    
    for whale in whales:
        if whale > cur_floor + k or whale < cur_floor - k:
            groups.append(list())
            idx += 1
            cur_floor = whale
        
        groups[idx].append(whale)

    return len(max(groups, key = lambda x: len(x)))


def solve(whales, num_whales, k):
    # Count the number of groups within k of each other, then use the length of the biggest group.
    
    whales.sort() # algorithm requires a sorted array
    l1 = x(whales, k)
    whales.reverse() # check both forwards and backwards, as there may be a better grouping from back to front
    l2 = x(whales, k)
    

    return num_whales - max(l1, l2)


def main():
    for _ in range(int(input())):
        num_whales, k = map(int, input().split())
        whales = list(map(int, input().split()))
        
        print(solve(whales, num_whales, k))
        input()
        
main()
