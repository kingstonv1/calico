def trib_positive(n, first, second, third, count):
    if count == n:
        return third

    return trib_positive(n, second, third, (first + second + third), count + 1)


def trib_negative(n, first, second, third, count):
    if count == n:
        return first
    
    return trib_negative(n, (third - second - first), first, second, count - 1)


for _ in range(int(input())):
    i = int(input())
    
    if i in (0, 1):
        print(i)
        continue
        
    print(trib_positive(i, -1, 0, 1, 1) if i >= 0 else trib_negative(i, 1, 0, 1, 1))
    