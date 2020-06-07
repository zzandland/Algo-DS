from collections import defaultdict

class Node:
    def __init__(self):
        self.next = defaultdict(Node)
        self.top3 = []

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.cur = Node()
        self.id_ = 0
        self.query = ''
        self.query2id = {}
        self.id2query = {}
        self.id2cnt = {}
        self.comp = lambda id_: (-self.id2cnt[id_], self.id2query[id_])
        for s, t in zip(sentences, times):
            self._update(s, t)
        
    def _query2id(self, query: str) -> int:
        if query not in self.query2id:
            self.query2id[query] = self.id_
            self.id2query[self.id_] = query
            self.id2cnt[self.id_] = 0
            self.id_ += 1
        return self.query2id[query]
    
    def _update(self, query: str, times: int = 1) -> None:
        id_ = self._query2id(query)
        self.id2cnt[id_] += times
        n = self.root
        for c in query:
            n = n.next[c]
            if id_ not in n.top3:
                if len(n.top3) < 3:
                    n.top3.append(id_)
                else:
                    minIdx = max(range(3), key=lambda i: self.comp(n.top3[i]))
                    if self.comp(id_) <= self.comp(n.top3[minIdx]):
                        n.top3[minIdx] = id_

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.query += c
            self.cur = self.cur.next[c]
            return [self.id2query[id_] for id_ in sorted(self.cur.top3, key=self.comp)]
        else:
            self._update(self.query)
            self.query = ''
            self.cur = self.root

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)