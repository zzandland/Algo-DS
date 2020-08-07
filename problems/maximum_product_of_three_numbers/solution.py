class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l1 = l2 = l3 = float('-inf')
        s1 = s2 = float('inf')
        for n in nums:
            if n > l1: l1, l2, l3 = n, l1, l2
            elif n > l2: l2, l3 = n, l2
            elif n > l3: l3 = n
                
            if n < s1: s1, s2 = n, s1
            elif n < s2: s2 = n
        return max(l1*l2*l3, s1*s2*l1)