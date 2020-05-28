class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if not nums: return -1
        def findPivot() -> int:
            l, r = 0, N-1
            while l < r:
                m = l + (r-l)//2
                if nums[m] > nums[m+1]: return m
                elif nums[m] > nums[l]: l = m+1
                else: r = m    
            return l if l == N-1 else l+1
        p = findPivot()
        if target >= nums[0]: l, r = 0, p
        else: l, r = p+1, N-1
        while l <= r:
            m = l + (r-l)//2    
            if nums[m] == target: return m
            if nums[m] < target: l = m+1
            else: r = m-1
        return -1