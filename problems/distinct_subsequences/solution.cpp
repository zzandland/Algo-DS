class Solution {
public:
    int numDistinct(string s, string t) {
        int S = s.length(), T = t.length();
        vector<vector<unsigned long>> dp(T+1, vector<unsigned long>(S+1, 0));
        for (int i = 0; i <= S; ++i) {
            dp[T][i] = 1;
        }
        for (int i = T-1; i >= 0; --i) {
            for (int j = S-1; j >= 0; --j) {
                dp[i][j] = dp[i][j+1];
                if (s[j] == t[i]) dp[i][j] += dp[i+1][j+1];
            }
        }
        return dp[0][0];
    }
};