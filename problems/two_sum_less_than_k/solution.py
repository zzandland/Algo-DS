class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        l, r = 0, len(A)-1
        res = -1
        while l < r:
            sm = A[l] + A[r]
            if sm < K: res = max(res, sm)
            if sm > K: r -= 1
            else: l += 1
        return res