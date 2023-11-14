from collections import defaultdict


def solve(words):
    syls = sorted(words.keys())
    temp_storage = dict()
    print(words)
    
    p1, p2 = 0, len(words) - 1
    
    
    


for _ in range(int(input())):
    w = defaultdict(lambda: [])
    
    for _ in range(int(input())):
        syl, word = input().split()
        w[int(syl)].append(word)
        
    print(solve(w))
    