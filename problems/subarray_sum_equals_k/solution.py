from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        run, res, dic = 0, 0, Counter({0: 1})
        for num in nums:
            run += num
            res += dic[run-k]
            dic[run] += 1
        return res