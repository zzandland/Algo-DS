from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = Counter({0: 1})
        run = res = 0
        for n in nums:
            run += n
            res += seen[run - k]
            seen[run] += 1
        return res