def solve(chains, target, heights, lows):
    global sausages
    
    sausages = [0 for _ in range(max(heights))]
    
    for i in range(chains):
        for x in range(lows[i], heights[i]):
            sausages[x] += 1
    
    for i in range(1, len(sausages)):
        for x in range(1, len(sausages)):
            if sum(sausages[i:x + 1]) > target:
                break
            
            if sum(sausages[i:x + 1]) == target:
                return (i, x + 1)

    return "IMPOSSIBLE"


sausages = list()

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    
    n = nums[0]
    k = nums[1]
    highs = list(map(int, input().split()))
    lows = list(map(int, input().split()))
    
    ans = solve(n, k, highs, lows)
    
    print(ans if ans == "IMPOSSIBLE" else f'{ans[0]} {ans[1]}')