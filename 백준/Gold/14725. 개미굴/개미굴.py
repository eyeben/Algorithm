ans = []
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def display(self):
        node = self.root
        def __display(node, cnt = 1):
            if node.children:
                for itm in sorted(list(node.children.keys())):
                    print((cnt-1)*'--'+itm)
                    __display(node.children[itm], cnt+1)
        __display(node)



N = int(input())
T = Trie()
for i in range(N):
    li = input().split()[1:]
    T.insert(li)



T.display()
for itm in ans:
    print(itm)