def solve(whales, num_whales, k):
    high, low = 0, 0
    m = float('-inf')
    
    whales.sort()
    
    while high < num_whales:
        
        if whales[high] - whales[low] > k:
            low += 1
        else:
            high += 1

        m = max(high - low, m)
            
    return num_whales - m

def main():
    
    for _ in range(int(input())):
        num_whales, k = map(int, input().split())
        whales = list(map(int, input().split()))
        
        print(solve(whales, num_whales, k))
        input()
        
main()
