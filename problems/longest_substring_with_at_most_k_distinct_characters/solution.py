from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dic, j, mx = Counter(), 0, 0
        for i, c in enumerate(s):
            dic[c] += 1
            while len(dic.keys()) > k:
                dic[s[j]] -= 1
                if dic[s[j]] == 0: del dic[s[j]]
                j += 1
            mx = max(mx, i-j+1)        
        return mx    