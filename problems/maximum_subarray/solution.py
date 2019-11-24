class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    output, current = float('-inf'), 0
    for num in nums:
      if current < 0:
        current = num
      else:  
        current += num  
      output = max(output, current)  
    return output   