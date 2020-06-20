class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res, st = 0, [float('inf')]
        for n in arr:
            while st[-1] <= n:
                mn = st.pop()
                res += mn * min(n, st[-1])
            st.append(n)
        while len(st) > 2:
            res += st.pop() * st[-1]
        return res