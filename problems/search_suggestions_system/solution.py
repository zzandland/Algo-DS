from heapq import heappush, nsmallest
from collections import defaultdict

class Trie:
    def __init__(self):
        self.next = defaultdict(Trie)
        self.words = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # create trie of all characters in products O(products * longest word product)
        trie = Trie()
        for product in products:
            n = trie
            for c in product:
                heappush(n.words, product)
                n = n.next[c]
            heappush(n.words, product)
            
        res = []
        n = trie
        for c in searchWord:
            n = n.next[c]
            res.append(nsmallest(3, n.words))
            
        return res