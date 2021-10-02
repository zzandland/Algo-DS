class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int I = s1.length(), J = s2.length(), K = s3.length();
        if (I + J != K) return false;
        vector<vector<bool>> dp(I+1, vector<bool>(J+1, false));
        dp[0][0] = true;
        for (int i = 0; i <= I; ++i) {
            for (int j = 0; j <= J; ++j) {
                if (i == 0 && j == 0) {
                    dp[i][j] = true;
                } else if (i == 0) {
                    dp[i][j] = dp[i][j-1] && s2[j-1] == s3[j-1];
                } else if (j == 0) {
                    dp[i][j] = dp[i-1][j] && s1[i-1] == s3[i-1];
                } else {
                    dp[i][j] = (
                        dp[i-1][j] && s1[i-1] == s3[i+j-1] ||
                        dp[i][j-1] && s2[j-1] == s3[i+j-1]
                    );
                }
            }
        }
        return dp[I][J];
    }
};