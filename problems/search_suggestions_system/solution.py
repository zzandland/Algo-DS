from collections import defaultdict
from heapq import heappush, nsmallest

class Trie:
    def __init__(self):
        self.products = []
        self.next = defaultdict(Trie)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for prod in products:
            n = trie
            for c in prod:
                n.products.append(prod)
                n = n.next[c]
            n.products.append(prod)
        res = []
        n = trie
        for c in searchWord:
            n = n.next[c]
            res.append(nsmallest(3, n.products))
        return res