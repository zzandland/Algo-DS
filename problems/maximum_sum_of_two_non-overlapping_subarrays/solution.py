class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # 0 6 5 2 2 1 9 2 3 L 3 R 2
        
        # 0 0 6 11 13 15 16 25 27 30
        # 0 6 5 / 2 2 1 9 2 3
        # 0 6 5 2 / 2 1 9 2 3
        # 0 6 5 2 2 1 9 / 2 3
        N = len(A)
        
        # get prefix sum
        pf = [0]
        for n in A:
            pf.append(pf[-1] + n)
            
        def helper(L: int, M: int) -> int:
            # get max sm for each interval L and M
            left = [0]
            for i in range(L, N-M+1):
                left.append(max(left[-1], pf[i] - pf[i-L]))
            left = left[1:]
            right = [0]
            for i in range(N-M, L-1, -1):
                right.append(max(right[-1], pf[i+M] - pf[i]))
            right = right[1:][::-1]
            return max(a + b for a, b in zip(left, right))
        
        return max(helper(L, M), helper(M, L))