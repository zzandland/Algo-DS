from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return list(filter(lambda x: x[1] == 1, c.items()))[0][0]