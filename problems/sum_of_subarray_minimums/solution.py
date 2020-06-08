class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        N, st, res = len(A), [], 0
        prev, nxt = [i for i in range(1, N+1)], [i for i in range(N, 0, -1)]
        for i, n in enumerate(A):
            while st and st[-1][1] >= n:
                j, _ = st.pop()
                nxt[j] = i-j
            if st:
                prev[i] = i - st[-1][0]
            st.append((i, n))
        for i, j, k in zip(A, prev, nxt):
            res += i*j*k 
        return res % (10**9+7)