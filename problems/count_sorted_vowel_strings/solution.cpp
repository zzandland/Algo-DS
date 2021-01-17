class Solution {
public:
    int countVowelStrings(int n) {
        if (n == 1) return 5;
        int dp[n][5];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < 5; ++j) {
                if (i == 0) {
                    dp[i][j] = 1;  
                } else {
                    dp[i][j] = 0;
                    for (int k = j; k < 5; ++k) {
                        dp[i][j] += dp[i-1][k];
                    }
                }
            }
        }
        int res = 0;
        for (int i = 0; i < 5; ++i) {
            res += dp[n-1][i];  
        }
        return res;
    }
};