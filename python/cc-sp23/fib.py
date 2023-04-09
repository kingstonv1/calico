def fibonacci(n):
    """
    Returns a list of Fibonacci numbers up to the nth index.
    """
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def solve(N, Q):
    fib = fibonacci(N)
    zeros = [0 for _ in range(N)]

    for _ in range(Q):
        LR = list(map(int, input().split()))
        L = LR[0]
        R = LR[1]

        index = 0

        for i in range(L - 1, R):
            add = fib[index]
            zeros[i] += add
            index += 1

    for i in range(len(zeros)):
        zeros[i] %= 998244353

    return zeros


for _ in range(int(input())):
    NQ = list(map(int, input().split()))
    N = NQ[0]
    Q = NQ[1]

    print(" ".join(list(map(str, solve(N, Q)))))
