class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mx = min(steps//2+1, arrLen)
        q = [0]*mx
        q[0] = 1
        for _ in range(steps):
            nq = [0]*mx
            for i in range(mx):
                if i > 0: nq[i-1] += q[i]
                nq[i] += q[i]
                if i < mx - 1: nq[i+1] += q[i]
            q = nq
        return q[0] % (10**9+7)