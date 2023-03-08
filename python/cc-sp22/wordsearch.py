def solve(ws, s, c):
    ans = list()
    
    for line in ws:
        if s not in line:
            ans.append('#' * c)
        else:
            startind = line.find(s)
            temp = '#' * c
            ans.append(temp[:startind] + s + temp[startind + len(s):])
    
    return ans

for _ in range(int(input())):
    hidden = input()
    wordsearch = list()
    rowcol = list(map(int, input().split()))
    
    for row in range(rowcol[0]):
        wordsearch.append(input())
    
    solved = solve(wordsearch, hidden, rowcol[1])
    
    for string in solved:
        print(string)
    
    print()
    
    input()