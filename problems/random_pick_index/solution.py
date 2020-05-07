from collections import defaultdict
from random import randrange

class Solution:
    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:
        return self.dic[target][randrange(len(self.dic[target]))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)