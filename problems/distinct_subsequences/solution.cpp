class Solution {
public:
    int numDistinct(string s, string t) {
        int S = s.length(), T = t.length();
        vector<vector<unsigned>> dp(T + 1, vector<unsigned>(S + 1, 0));
        for (int i = 0; i <= S; ++i) {
            dp[0][i] = 1;
        }
        for (int y = 1; y <= T; ++y) {
            for (int x = 1; x <= S; ++x) {
                if (t[y-1] == s[x-1]) dp[y][x] += dp[y-1][x-1];
                dp[y][x] += dp[y][x-1];
            }
        }
        return dp[T][S];
    }
};    
