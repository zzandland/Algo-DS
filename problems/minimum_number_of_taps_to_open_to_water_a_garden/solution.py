class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ints = []
        for i, c in enumerate(ranges):
            ints.append([max(0, i-c), min(n, i+c)])
        dp = [(0, 0)]
        ints.sort(key=lambda x: (x[0], -x[1]))
        for u, v in ints:
            idx = bisect.bisect_left(dp, (u, ))
            if idx == len(dp): return -1
            if dp[-1][0] < v: dp.append((v, dp[idx][1] + 1))
        return dp[-1][1]