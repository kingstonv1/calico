def insertionSort(arr):
    keys = []
    for i in range (len(arr)):
        keys.append(i + 1)
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                keys[j+1] = keys[j]
                j -= 1
        arr[j+1] = key
        keys[j+1] = key
        
        return [arr, keys]
        
def solve (N, C):
    """
    Output the minimum total wait time on the first line.
    Output the optimal new permutation on the second line.
    
    N: the number of students in line
    C: the list of the bottle capacities, in liters, for each student
    """
    minWait = 0
    
    things = insertionSort(C)
    
    sortedLine, sortedKeys = things[0], things[1]
    
    for i in range (N):
        minWait += (C[i] + minWait)
    
    print(minWait)
    for i in sortedKeys:
        print(i, end=" ")

def main ():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = [int(C_i) for C_i in input().split()]
        solve(N, C)

if __name__ == '__main__':
    main()