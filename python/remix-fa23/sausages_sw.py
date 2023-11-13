def solve(n, k, highs, lows):
    max_height = max(highs)
    sausages = [0 for _ in range(max_height)]
    
    for i in range(n):
        for x in range(lows[i], highs[i]):
            sausages[x] += 1
    
    high, low = 1, 1
    s = sausages[1]
    
    while high < len(sausages):
        if s == k:
            return low, high + 1

        if s < k:
            high += 1
            
            if high < len(sausages):
                s += sausages[high]
                
        else:
            s -= sausages[low]
            low += 1

    return "IMPOSSIBLE"


def main():
    for _ in range(int(input())):
        nums = list(map(int, input().split()))
        
        n = nums[0]
        k = nums[1]
        highs = list(map(int, input().split()))
        lows = list(map(int, input().split()))
        
        ans = solve(n, k, highs, lows)
        
        print(ans if ans == "IMPOSSIBLE" else f'{ans[0]} {ans[1]}')
        
        
main()