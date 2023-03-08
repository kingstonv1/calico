def solve(timeSpan, menu, days):
    amounts = set()
    
    for day in range(timeSpan):
        count = 0
        
        for i in range(days):
            try:
                if menu[day + i] == 0:
                    break
                
                count += menu[day + i]
            except:
                pass

        amounts.add(count)
    

    return max(amounts)

for _ in range(int(input())):
    i = list(map(int, input().strip().split()))
    n, k, d = (i[0], i[1], i[2])
    meals = list(map(int, input().strip().split()))
    
    print(solve(n, meals, d))