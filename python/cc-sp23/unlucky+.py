class TrieNode:
    def __init__(self):
        self.children = [None] * 9
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            idx = int(ch) - 2
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True


def find_largest_number(d, trie):
    result = []
    curr = trie.root
    for i in range(d):
        found = False
        for j in range(8):
            if not curr.children[j]:
                result.append(j+2)
                curr = trie.root
                found = True
                break
        if not found:
            result.append(9)
            curr = curr.children[7]
    return ''.join(map(str, result))


t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    trie = Trie()
    for _ in range(n):
        unlucky_num = input().strip()
        trie.insert(unlucky_num)
    print(find_largest_number(d, trie))