class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int N = triangle.size();
        vector<vector<int>> dp(N+1);
        for (int i = 0; i < N; ++i) dp[i] = vector<int>(i+1, INT_MAX);
        dp[N] = vector<int>(N+1, 0);
        for (int i = N-1; i >= 0; --i) {
            for (int j = 0; j < i+1; ++j) {
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1]);
            }
        }
        return dp[0][0];
    }
};