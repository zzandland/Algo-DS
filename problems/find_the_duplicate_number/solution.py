class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = t = 0
        while True:
            h, t = nums[nums[h]], nums[t]
            if h == t: break
        t = 0
        while h != t:
            h, t = nums[h], nums[t]
        return h