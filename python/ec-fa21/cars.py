def solve(cars):
    clumps = 0
    chain = False
    
    for i in range(1, len(cars)):
        if cars[i - 1] == cars[i]:
            if chain == False:
                clumps += 1
                chain = True
                
        elif cars[i] > cars[i - 1]:            
            cars[i] = cars[i - 1]
            clumps += 1
            chain = False
        
        else:
            clumps += 1
            chain = False
    
    return clumps

for _ in range(int(input())):
    i = input().split()
    cars = list(map(int, i[1].split(',')))
    
    print(solve(cars))
