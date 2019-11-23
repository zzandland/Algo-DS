class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      cache, output = {}, []
      for num in nums1:
        if num in cache:
          cache[num] += 1
        else:
          cache[num] = 1  
      for num in nums2:
        if num in cache and cache[num] > 0:
          output += [num]    
          cache[num] -= 1
      return output    