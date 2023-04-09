def is_unlucky(number, unlucky_numbers):
    for unlucky in unlucky_numbers:
        if str(unlucky) in number:
            return True
    return False

def find_largest_number(D, unlucky_numbers):
    for num in range(10 ** (D - 1), 10 ** D)[::-1]:
        if not is_unlucky(str(num), unlucky_numbers):
            return num

T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    unlucky_numbers = list(map(int, input().split()))
    print(find_largest_number(D, unlucky_numbers))
