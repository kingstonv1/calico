# Working!

t = int(input())

sentences = []
solved = []

for i in range (t):
    string = input()
    sentences.append(string.split())
    
for strings in sentences:
    longest = max(strings, key=len)
    dim = len(longest) + 2
    sol = ""
    sol += dim*'*'
    
    for string in strings:
        sol += '\n'
        string = '*' + string + (len(longest) - len(string))*' ' + '*'
        sol += string
    sol += '\n'
    sol += dim*'*'
    
    solved.append(sol)

for i in solved:
    print(i)