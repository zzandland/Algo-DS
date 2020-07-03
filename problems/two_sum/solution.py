class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            l = target - n
            if l in dic: return [dic[l], i]
            dic[n] = i