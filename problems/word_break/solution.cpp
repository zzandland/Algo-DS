class Solution {
public:
    bool helper(int i, string s, unordered_set<string>& ws, unordered_map<int, int>& dp) {
        if (i > s.length()) return 0;
        if (i == s.length()) return 1;
        if (!dp.count(i)) {
            for (int j = 1; i+j <= s.length(); ++j) {
                if (ws.count(s.substr(i, j)) && helper(i+j, s, ws, dp)) {
                    dp[i] = 1;
                    break;
                }
            }
            if (!dp.count(i)) dp[i] = 0;
        }
        return dp[i];
    }

    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> ws;
        for (string w : wordDict) ws.emplace(w);
        const int ln = s.length();
        bool dp[ln + 1];
        memset(dp, 0, ln + 1);
        dp[0] = true;
        for (int i = 0; i <= ln; ++i) {
            for (int j = 0; j < i; ++j) {
                if (ws.count(s.substr(j, i-j)) && dp[j]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
};