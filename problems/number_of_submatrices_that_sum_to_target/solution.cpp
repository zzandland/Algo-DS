class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        if (!matrix.size()) return 0;
        int m = matrix.size(), n = matrix[0].size(), res = 0;
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        for (int y = 0; y < m; ++y)
            for (int x = 0; x < n; ++x)
                dp[y+1][x+1] = dp[y+1][x] + dp[y][x+1] - dp[y][x] + matrix[y][x];
        
        unordered_map<int, int> freq;
        for (int r = 1; r <= m; ++r) {
            for (int y = 0; y < r; ++y) {
                freq.clear();
                ++freq[0];
                for (int x = 1; x <= n; ++x) {
                    int tmp = dp[r][x] - dp[y][x];
                    res += freq[target - tmp];
                    ++freq[-tmp];
                }
            }
        }
        return res;
    }
};