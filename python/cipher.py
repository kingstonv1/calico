import re

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = re.compile(r'-?\d+')

def getNum(s):
    return int(numbers.search(s).group())

def solve(cy, steps):
    cy = list(cy)
    steps.reverse()
    
    for step in steps:
        if 'C' in step:
            offset = getNum(step)
            
            for i in range(len(cy)):
                if not cy[i].isalpha():
                    continue
                
                let = alpha.index(cy[i])
                cy[i] = alpha[(let - offset) % len(alpha)]

        elif 'A' in step:
            for i in range(len(cy)):
                if not cy[i].isalpha():
                    continue
                
                let = alpha.index(cy[i])
                cy[i] = alpha[-let - 1]
    
        elif 'R' in step:
            cy.reverse()
    
    return "".join(cy)
            

for _ in range(int(input())):
    cypher = input()
    input()
    print(solve(cypher.lower(), input().split()))
    input()