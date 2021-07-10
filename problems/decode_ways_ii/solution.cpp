#define MOD 1000000007

class Solution {
public:
    int numDecodings(string s) {
        vector<int> dp(s.length(), -1);
        int res = dfs(s, 0, dp) % MOD;
        return res;
    }
    
    long dfs(const string &s, int i, vector<int> &dp) {
        if (i == s.length()) return 1;
        if (dp[i] == -1) {
            long res = 0;
            char c = s[i];
            if (c != '0') res += (c == '*' ? 9 : 1) * dfs(s, i+1, dp);
            if (i < s.length() - 1) {
                string ss = s.substr(i, 2);
                if (ss == "**") {
                    res += 15 * dfs(s, i + 2, dp);
                } else if (ss[0] == '*') {
                    int oneth = ss[1] - '0';
                    res += (oneth < 7 ? 2 : 1) * dfs(s, i + 2, dp);
                } else {
                    int tenth = ss[0] - '0', oneth = ss[1] - '0';
                    if (tenth == 1)
                        res += (ss[1] == '*' ? 9 : 1) * dfs(s, i + 2, dp);
                    else if (tenth == 2 && oneth < 7)
                        res += (ss[1] == '*' ? 6 : 1) * dfs(s, i + 2, dp);
                }
            }
            dp[i] = (res % MOD);
        }
        return dp[i];
    }
};