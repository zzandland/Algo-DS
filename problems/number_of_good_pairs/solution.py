from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter()
        res = 0
        for n in nums:
            res += c[n]
            c[n] += 1
        return res