for _ in range(int(input())):
    cards = [i for i in range(1, 501)]

    for _ in range(210):
        print('draw')

        for i in list(map(int, input().split())):
            try:
                cards.remove(i)
            except:
                pass

    for _ in range(48):
        if cards:
            print(f'check {cards[0]}')
            cards.pop(0)
            if input() == 'ABSENT':
                break
        else:
            break
input()
