from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        
        c = Counter(nums)
        
        for x in c:
            if k > 0 and x + k in c: res += 1
            elif k == 0 and c[x] > 1: res += 1
        return res