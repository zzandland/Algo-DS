class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) < 2: return sum(arr)
        q, res = [n for n in arr], 0
        while len(q) > 1:
            N = len(q)
            _, i = min([(q[i]+q[i+1], i) for i in range(N-1)], key=lambda x: x[0])
            res += q[i]*q[i+1]
            q = q[:i] + [(max(q[i], q[i+1]))] + q[i+2:]
        return res    