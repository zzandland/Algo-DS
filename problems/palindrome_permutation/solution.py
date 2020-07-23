from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        return len(list(filter(lambda x: x & 1 == 1, c.values()))) < 2