def solve (N, C):
    """
    Output the minimum total wait time on the first line.
    Output the optimal new permutation on the second line.
    
    N: the number of students in line
    C: the list of the bottle capacities, in liters, for each student
    """
    
    drinks = []
    order = []
    totalWaitTime = 0
    waitTime = 0
    orderStr = ""
    index = 0
    for x in C:
        index += 1
        drinks.append(tuple((index, x)))
    
    for i in range(1, len(drinks)):
        key = drinks[i][1]
        full = drinks[i]          
        j = i - 1
        while j >= 0 and key < drinks[j][1]:
                drinks[j+1] = drinks[j]
                j -= 1
        drinks[j + 1] = full
    
    for i in range(len(drinks)):
        order.append(drinks[i][0])
        waitTime += drinks[i][1]
        totalWaitTime += waitTime
        
    for i in range(len(order)):
        if i != len(order) - 1:
            orderStr = orderStr + str(order[i]) + " "
        else:
            orderStr = orderStr + str(order[i])
    print (str(totalWaitTime) + "\n" + orderStr)
    return 0

def main ():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = [int(C_i) for C_i in input().split()]
        solve(N, C)

if __name__ == '__main__':
    main()