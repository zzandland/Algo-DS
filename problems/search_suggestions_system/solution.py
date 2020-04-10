from collections import defaultdict

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = defaultdict(list)
        for product in products:
            for i in range(1, len(product)+1):
                t[product[:i]].append(product)
        return [sorted(t[searchWord[:j]])[:3] for j in range(1, len(searchWord)+1)]