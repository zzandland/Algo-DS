class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<int>> dp(s.length() + 1, vector<int>(p.length(), -1));
        return dfs(s, p, 0, 0, dp);
    }
    
    bool dfs(string &s, string &p, int i, int j, vector<vector<int>> &dp) {
        if (s.length() == i && p.length() == j) return true;
        if (s.length() < i || p.length() <= j) return false;
        if (dp[i][j] == -1) {
            if (p[j] == '*') {
                dp[i][j] = dfs(s, p, i+1, j, dp) ||
                           dfs(s, p, i, j+1, dp) ||
                           dfs(s, p, i+1, j+1, dp);
            } else {
                if (s.length() == i || p.length() == j) dp[i][j] = 0;
                else if (p[j] == '?') dp[i][j] = dfs(s, p, i+1, j+1, dp);
                else dp[i][j] = s[i] == p[j] && dfs(s, p, i+1, j+1, dp);  
            } 
        }
        return dp[i][j];
    }
};