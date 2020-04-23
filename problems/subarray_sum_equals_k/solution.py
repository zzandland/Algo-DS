from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        curSum, dic, output = 0, Counter(), 0
        for num in nums:
            curSum += num
            if curSum == k: output += 1
            diff = curSum - k    
            if diff in dic: output += dic[diff]
            dic[curSum] += 1    
        return output    