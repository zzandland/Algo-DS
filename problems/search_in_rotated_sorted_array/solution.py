class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        N = len(nums)
        l, r = 0, N-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[m+1]: l = r = m
            elif nums[m] >= nums[0]: l = m+1
            else: r = m
        if target >= nums[0]: a, b = 0, l
        else: a, b = l+1, N-1
        while a <= b:
            m = a + (b-a)//2
            if nums[m] == target: return m
            if nums[m] < target: a = m+1
            else: b = m-1
        return -1        