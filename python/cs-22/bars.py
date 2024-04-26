# Base & Bonus 1 Solved! Bonus 2 Bugged?
import math
import sys

sys.set_int_max_str_digits(0)

def solve(n):
    return (math.isqrt(8 * n + 1) - 1) // 2


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
    
