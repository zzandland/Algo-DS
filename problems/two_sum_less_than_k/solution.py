class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        l, r = 0, len(A)-1
        mx = -1
        while l < r:
            S = A[l] + A[r]
            if S < K: mx = max(mx, S)
            if S >= K: r -= 1
            else: l += 1
        return mx