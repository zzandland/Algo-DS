class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ''
        for w in d:
            i = j = 0
            while i < len(s) and j < len(w):
                if s[i] == w[j]: j += 1
                i += 1
            if j == len(w):
                if len(w) > len(res): res = w
                elif len(w) == len(res) and w < res: res = w
        return res