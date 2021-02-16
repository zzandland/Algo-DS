class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string> res;
        string tmp;
        dfs(0, tmp, S, res);
        return res;
    }
    
    void dfs(int i, string &tmp, string &S, vector<string> &res) {
        if (i == S.length()) {
            res.push_back(tmp.substr(0, tmp.length()));
            return;
        }
        if (isalpha(S[i])) {
            tmp.push_back(toupper(S[i]));
            dfs(i+1, tmp, S, res);
            tmp.pop_back();
            tmp.push_back(tolower(S[i]));
            dfs(i+1, tmp, S, res);
            tmp.pop_back();
        } else {
            tmp.push_back(S[i]);
            dfs(i+1, tmp, S, res);
            tmp.pop_back();
        }
    }
};