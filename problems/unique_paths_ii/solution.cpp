class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size()
          , n = obstacleGrid[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        dp[0][1] = 1;
        for (int y = 1; y <= m; ++y) {
            for (int x = 1; x <= n; ++x) {
                dp[y][x] = obstacleGrid[y-1][x-1] == 1
                    ? 0 
                    : dp[y-1][x] + dp[y][x-1];
            }
        }
        return dp[m][n];
    }
};