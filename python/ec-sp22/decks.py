import math
for _ in range(int(input())):
    n = int(input())
    m = math.ceil(n * (n + 1) // 2)
    print(math.ceil((((m * 3) - n) + 53) // 54))
