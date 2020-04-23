from collections import Counter

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff, dic, longest = 0, Counter(), 0
        for i, num in enumerate(nums):
            diff += 1 if num == 1 else -1
            if diff == 0: 
                longest = i+1
            else:    
                if diff in dic: longest = max(longest, i-dic[diff])
                else: dic[diff] = i    
        return longest            