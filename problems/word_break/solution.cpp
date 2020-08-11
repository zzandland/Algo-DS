class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> st;
        for (string w: wordDict) st.emplace(w);
        
        int len = s.size();
        
        bool dp[len+1];
        fill_n(dp, len+1, false);
        dp[0] = true;
        for (int i = 0; i < len; ++i) {
            for (int j = i; j >= 0; --j) {
                if (st.count(s.substr(j, i-j+1)) && dp[j]) {
                    dp[i+1] = true;  
                    break;
                } 
            }
        }
        
        return dp[s.size()];
    }
};