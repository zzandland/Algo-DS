class Solution {
public:
    int minDistance(string word1, string word2) {
        int a = word1.length(), b = word2.length();
        vector<vector<int>> dp(a+1, vector<int>(b+1, 0));
        for (int i = 0; i < a; ++i) {
            for (int j = 0; j < b; ++j) {
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]);
                if (word1[i] == word2[j]) dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j+1]);
            }
        }
        return word1.length() + word2.length() - 2 * dp[a][b];
    }
};