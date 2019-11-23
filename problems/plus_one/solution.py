class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    lift = 1
    output = []
    for digit in digits[::-1]:
      digit += lift
      if digit == 10:
        digit = 0
        lift = 1
      else:
        lift = 0  
      output = [digit] + output  
    if lift == 1:
      output = [1] + output  
    return output