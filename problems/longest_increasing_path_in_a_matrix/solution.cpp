class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dp[i][j] == 0) res = max(res, dfs(i, j, matrix, dp));
            }
        }
        return res;
    }
    
    int dfs(int y, int x, const vector<vector<int>>& matrix, vector<vector<int>>& dp) {
        int m = matrix.size(), n = matrix[0].size();
        if (dp[y][x] == 0) {
            int res = 1;
            int dir[] = {-1, 0, 1, 0, -1};
            for (int i = 0; i < 4; ++i) {
                int ny = y + dir[i], nx = x + dir[i+1];
                if (0 <= ny && ny < m && 0 <= nx && nx < n && matrix[y][x] < matrix[ny][nx])
                    res = max(res, 1 + dfs(ny, nx, matrix, dp));
            }
            dp[y][x] = res;
        }
        return dp[y][x];
    }
};