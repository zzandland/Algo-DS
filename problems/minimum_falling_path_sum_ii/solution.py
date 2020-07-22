class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        N = len(arr)
        dp = [0]*N
        for y in range(N):
            ndp = dp[:]
            fst, scd = (float('inf'), 0), (float('inf'), 0)
            for i, x in enumerate(dp):
                if x < fst[0]:
                    scd = fst
                    fst = (x, i)
                elif x < scd[0]:
                    scd = (x, i)
            for i in range(N):
                if i != fst[1]: ndp[i] = fst[0] + arr[y][i]
                else: ndp[i] = scd[0] + arr[y][i]
            dp = ndp
        return min(dp)