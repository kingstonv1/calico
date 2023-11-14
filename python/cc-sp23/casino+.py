import random

for _ in range(int(input())):
    cards = [i for i in range(1, 501)]
    count = 0

    for _ in range(62):
        print('draw')

        for i in list(map(int, input().split())):
            try:
                cards.remove(i)
            except:
                pass

    random.shuffle(cards)

    while True:
        if cards:
            print(f'check {cards[0]}')
            cards.pop(0)
            if input() == 'ABSENT':
                break
        else:
            break
input()
