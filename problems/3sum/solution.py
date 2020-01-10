class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    output = []
    if len(nums) > 2:
      o = set()
      nums.sort()
      for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
          continue
        l, r = i + 1, len(nums) - 1
        while l < r:
          lNum, rNum = nums[l], nums[r]
          totalSum = num + lNum + rNum
          if totalSum == 0:
            o.add((num, lNum, rNum))
          elif totalSum < 0:  
            l += 1
            continue
          r -= 1  
      for triple in o:
        output.append(list(triple))    
    return output    