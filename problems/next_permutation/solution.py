class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N == 0: return
        for i in range(N-1, -1, -1):
            if i == 0:
                nums.reverse()
                return
            if nums[i-1] < nums[i]: break
        l, r, t, found = i, N-1, nums[i-1], False
        while l < r:
            m = l + (r-l)//2
            if nums[m] > t and nums[m+1] <= t:
                found = True
                break
            if nums[m] > t: l = m+1
            else: r = m    
        if not found: m = l
        nums[i-1], nums[m] = nums[m], nums[i-1]        
        l, r = i, N-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1