from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N, c = len(nums), Counter(nums)
        for n, f in c.items():
            if f > N//2: return n