class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        N = len(nums)
        l, r = 0, N-1
        f = s = -1
        while l < r:
            m = l + (r-l)//2
            if nums[m] < target and nums[m+1] == target:
                f = m+1
                break
            elif nums[m] < target: l = m+1    
            else: r = m    
        if nums[l] == target: f = l
        l, r = 0, N-1        
        while l < r:
            m = l + (r-l)//2
            if nums[m] == target and nums[m+1] > target:
                s = m
                break
            elif nums[m] <= target: l = m+1    
            else: r = m
        if nums[r] == target: s = r        
        return [f, s]        