from collections import defaultdict

class Node:
    def __init__(self):
        self.top = []
        self.next = defaultdict(Node)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.id2s = {}
        self.s2id = {}
        self.s2cnt = {}
        self.id = 0
        self.root = Node()
        self.cur = self.root
        self.buf = ''
        for s, t in zip(sentences, times):
            self.genId(s)
            self.s2cnt[s] += t
            self.update(s)
            
    def genId(self, s: str) -> None:
        if s not in self.s2id:
            self.id2s[self.id] = s
            self.s2id[s] = self.id
            self.s2cnt[s] = 0
            self.id += 1

    def update(self, s: str) -> None:
        id, n = self.s2id[s], self.root
        for c in s:
            n = n.next[c]
            if id not in n.top:
                if len(n.top) < 3:
                    n.top.append(id)
                else:
                    n.top.sort(key=lambda x: (-self.s2cnt[self.id2s[x]], self.id2s[x]))
                    mn = n.top[-1]
                    scnt, mncnt = self.s2cnt[s], self.s2cnt[self.id2s[mn]]
                    if (-scnt, s) < (-mncnt, self.id2s[mn]): n.top[-1] = id

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.genId(self.buf)
            self.s2cnt[self.buf] += 1
            self.update(self.buf)
            self.buf = ''
            self.cur = self.root
        else:
            self.buf += c
            self.cur = self.cur.next[c]
            return sorted(list(map(lambda x: self.id2s[x], self.cur.top)), key=lambda x: (-self.s2cnt[x], x))

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)