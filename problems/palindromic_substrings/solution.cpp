class Solution {
public:
    int countSubstrings(string s) {
        int L = s.length();
        vector<vector<bool>> dp(L, vector<bool>(L, false));
        int res = 0;
        for (int i = 0; i < L; ++i) {
            dp[i][i] = true;
            if (i > 0) dp[i][i-1] = true;
        }
        for (int l = L-1; l >= 0; --l) {
            for (int r = l+1; r < L; ++r) {
                if (s[l] == s[r] && dp[l+1][r-1]) {
                    dp[l][r] = true;
                    ++res;
                }
            }
        }
        return res + L;
    }
};