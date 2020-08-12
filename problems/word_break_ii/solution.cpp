class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int N = s.size();
        
        unordered_set<char> a;
        for (char c: s) a.emplace(c);
        
        unordered_map<string, int> st;
        unordered_set<char> b;
        for (int i = 0; i < wordDict.size(); ++i) {
            st[wordDict[i]] = i;
            for (char c: wordDict[i]) b.emplace(c);
        } 
        
        vector<string> res;
        for (auto it = a.begin(); it != a.end(); ++it)
            if (!b.count(*it)) return res;
        
        vector<vector<vector<int>>> dp(N+1, vector<vector<int>>());
        int M = wordDict.size();
        dp[0].push_back({M});
        wordDict.push_back("");
        
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j <= i; ++j) {
                string ss = s.substr(j, i-j+1);
                if (st.count(ss)) {
                    for (vector<int> t: dp[j]) {
                        t.push_back(st[ss]);
                        dp[i+1].push_back(t);
                    }
                }
            }
        }
        
        for (int i = 0; i < dp[N].size(); ++i) {
            ostringstream os;
            for (int idx: dp[N][i]) {
                os << wordDict[idx] << ' ';
            }
            string x = os.str();
            res.push_back(x.substr(1, x.size()-2));
        }
        return res;
    }
};