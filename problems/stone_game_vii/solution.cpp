class Solution {
public:
    int stoneGameVII(vector<int>& stones) {
        int N = stones.size();
        vector<vector<int>> dp(N, vector<int>(N, 0));
        for (int i = N-2; i >= 0; --i) {
            int sum = stones[i];
            for (int j = i+1; j < N; ++j) {
                sum += stones[j];
                dp[i][j] = max(
                    sum - stones[i] - dp[i+1][j],
                    sum - stones[j] - dp[i][j-1]
                );
            }
        }
        return dp[0][N-1];
    }
};