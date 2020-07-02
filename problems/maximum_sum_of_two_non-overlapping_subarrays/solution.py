class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        for i in range(1, N):
            A[i] += A[i-1]
        res, lmax, mmax = A[L+M-1], A[L-1], A[M-1]
        for j in range(L+M, N):
            lmax = max(lmax, A[j-M]-A[j-L-M])
            mmax = max(mmax, A[j-L]-A[j-L-M])
            res = max(res, lmax + A[j]-A[j-M], mmax + A[j]-A[j-L])
        return res