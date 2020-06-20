from collections import defaultdict

class Node:
    def __init__(self):
        self.next = defaultdict(Node)
        self.wds = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        id2p, trie = {}, Node()
        for i, p in enumerate(products):
            n = trie
            id2p[i] = p
            for c in p:
                n = n.next[c]
                n.wds.append(i)
        n, res = trie, []
        for s in searchWord:
            n = n.next[s]
            res.append([id2p[id_] for id_ in n.wds[:3]])
        return res