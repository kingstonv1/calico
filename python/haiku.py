import itertools as it

words = {}


def solve():
    line1 = ""
    line2 = ""
    line3 = ""
    syl = int()

    for i in it.permutations(words.keys()):
        syl = 0
        line = ""

        for s in i:
            syl += words[s]
            line += (s + " ")

            if line1 != "" or line3 != "":
                if syl == 5:
                    if line1 == "":
                        line1 = line[:-1]
                        continue
                    if line3 == "":
                        line3 = line[:-1]
                        continue
            if line2 != "":
                if syl == 7:
                    line2 = line[:-1]
                    continue

            if "" not in {line1, line2, line3}:
                break
    if "" not in {line1, line2, line3}:
        return f"{line1}\n{line2}\n{line3}"
    else:
        return "IMPOSSIBLE"



for _ in range(int(input())):
    for _ in range(int(input())):
        i = input().strip().split()
        words[i[1]] = int(i[0])
    print(solve())
    words.clear()
