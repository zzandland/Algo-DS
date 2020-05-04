from collections import defaultdict

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        if not flights or not days: return 0
        N, K = len(days), len(days[0])
        dp = [0] * N
        for i in range(K-1, -1, -1):
            tmp = [0] * N
            for j in range(N):
                for k in range(N):
                    if j == k or flights[j][k]: tmp[j] = max(tmp[j], days[k][i] + dp[k])
            dp = tmp            
        return dp[0]