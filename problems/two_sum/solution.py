class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      s = {}
      for i, num in enumerate(nums):
        rem = target - num
        if str(rem) in s:
          return [s[str(rem)], i]
        else:
          s[str(num)] = i
      return []