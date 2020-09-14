class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        dp = [(0, 0)]
        for u, v in clips:
            idx = bisect.bisect_left(dp, (u,))
            if idx == len(dp): return -1
            if v > dp[-1][0]: dp.append((v, dp[idx][1] + 1))
            if dp[-1][0] >= T: return dp[-1][1]
        return -1