class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        M, N = len(nums1), len(nums2)
        if M == N == 0: return 0
        
        def handleEven(m: int, n: int) -> int:
            mm = nums1[m+1] if m+1 < M else float('inf')
            nn = nums2[n+1] if n+1 < N else float('inf')
            return min(mm, nn)
        
        odd = (M+N) & 1 == 1
        median = (M + N + 1) // 2
        if M and N and nums1[-1] <= nums2[0]:
            if not odd and N == M: return (nums1[-1] + nums2[0]) / 2
            n = (N-M)//2
            if odd: return nums2[n]
            return (nums2[n-1] + nums2[n]) / 2
        if M and N and nums2[-1] <= nums1[0]:
            if not odd and N == M: return (nums2[-1] + nums1[0]) / 2
            n = median-1
            if odd: return nums2[n]
            return (nums2[n] + nums2[n+1]) / 2
        
        l, r = median - M, median
        while l < r:
            mid = l + (r-l)//2
            n, m = mid - 1, median - mid - 1
            if n != N-1 and nums2[n] < nums1[m] < nums2[n+1]:
                if odd: return nums1[m]
                return (nums1[m] + handleEven(m, n)) / 2
            elif m != M-1 and nums1[m] < nums2[n] < nums1[m+1]:
                if odd: return nums2[n]
                return (nums2[n] + handleEven(m, n)) / 2
            elif nums2[n] < nums1[m]: l = mid+1
            else: r = mid
        n = min(l, r) - 1
        if odd: return nums2[n]
        m = median - n - 2
        return (nums2[n] + handleEven(m, n)) / 2