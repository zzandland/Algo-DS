from collections import defaultdict

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie, output = {}, []
        for pd in products:
            n = trie
            for c in pd:
                if c not in n:
                    n[c] = {}
                    n[c]['words'] = []
                n[c]['words'].append(pd)    
                n = n[c]
        n = trie        
        for ch in searchWord:
            if ch not in n: break
            output.append(sorted(n[ch]['words'])[:3])
            n = n[ch]
        while len(output) < len(searchWord): output.append([])    
        return output    