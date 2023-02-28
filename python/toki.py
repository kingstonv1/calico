import re

pona = re.compile(r'^(?:[mnptkswjl]?[aeiou]n?){1,}$')
ike = re.compile(r'(wu|wo|ji|ti|nn|nm|[aeiou][aeiou]|[bcfghqrvxyz])')

def solve(i):
    if ike.search(i) or not pona.search(i):
        return "ike"

    return "pona"

for _ in range(int(input())):
    print(solve(input()))