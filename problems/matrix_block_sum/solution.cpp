class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        for (int y = 0; y < m; ++y) {
            for (int x = 0; x < n; ++x) {
                dp[y+1][x+1] = dp[y+1][x] + dp[y][x+1] + mat[y][x] - dp[y][x];
            }
        }
        for (int y = 1; y <= m; ++y) {
            for (int x = 1; x <= n; ++x) {
                int xl = max(0, x - k - 1), xr = min(n, x + k);
                int yl = max(0, y - k - 1), yr = min(m, y + k);
                mat[y-1][x-1] = dp[yr][xr] - dp[yr][xl] - dp[yl][xr] + dp[yl][xl];
            }
        }
        return mat;
    }
};