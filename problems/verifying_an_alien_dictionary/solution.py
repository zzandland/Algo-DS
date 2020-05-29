class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        W = len(words)
        dic = {c: i for i, c in enumerate(order)}
        for i in range(1, W):
            a, b, found = words[i-1], words[i], False
            for j in range(min(len(a), len(b))):
                if dic[a[j]] > dic[b[j]]: return False
                if dic[a[j]] < dic[b[j]]: 
                    found = True
                    break
            if not found and j == len(b)-1: return False        
        return True    