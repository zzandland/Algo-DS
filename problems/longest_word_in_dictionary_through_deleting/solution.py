class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ''
        for t in d:
            if self.isSubSeq(s, t): res = min(res, t, key=lambda x: (-len(x), x))
        return res
    
    def isSubSeq(self, s: str, t: str) -> bool:
        j = 0
        for i, n in enumerate(s):
            if j == len(t):
                return True
            if n == t[j]:
                if j == len(t): return False
                j += 1
        return j == len(t)