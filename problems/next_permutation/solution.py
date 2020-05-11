class Solution:
    def partition(self, l: int, r: int, nums: List[int]) -> int:
        p, i = nums[r], l-1
        for j in range(l, r):
            if p > nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1
    
    def quickSort(self, l: int, r: int, nums: List[int]) -> None:
        if l < r:
            p = self.partition(l, r, nums)
            self.quickSort(l, p-1, nums)
            self.quickSort(p+1, r, nums)

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N < 2: return nums
        for i in range(N-2, -1, -1):
            if nums[i] < nums[i+1]: break
        if nums[i] >= nums[i+1]:
            for j in range(N//2):
                nums[j], nums[N-1-j] = nums[N-1-j], nums[j]
            return    
        nxt, nxtI = nums[i+1], i+1
        for j in range(i+1, N):
            if nums[j] > nums[i] and nxt > nums[j]: nxt, nxtI = nums[j], j
        nums[i], nums[nxtI] = nums[nxtI], nums[i]
        self.quickSort(i+1, N-1, nums)