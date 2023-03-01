import re

hi = re.compile(r'\b[iI]\'?[mM]\b')

def solve(s):
    s = s.strip()
    where = hi.search(s).end()
    return f"Hi {s[where + 1:]}, I'm dad."

    
for _ in range(int(input())):
    print(solve(input()))