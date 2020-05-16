class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        N = len(A)
        l, r = 0, N-1
        while l+1 < r:
            m = l + (r-l)//2
            if A[m-1] < A[m] > A[m+1]: return m
            if A[m-1] < A[m] < A[m+1]: l = m
            else: r = m    
        return -1        