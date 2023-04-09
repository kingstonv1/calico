for _ in range(int(input())):
    p = int(input())

    while True:
        while p < 160:
            print('buy')
            input()
            p += 60

        print('wish')
        p -= 160
        if 'baizhu' in input().split():
            input()
            break
