from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S, c, mx, j = len(s), Counter(), 0, 0
        for i in range(S):
            c[s[i]] += 1
            while c[s[i]] > 1:
                c[s[j]] -= 1
                j += 1
            mx = max(mx, i-j+1)    
        return mx    