class Solution {
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        vector<int> tmp(26), subset(26);
        vector<string> res;
        
        for (const string& b : B) {
            tmp = getCounter(b);
            for (int i = 0; i < 26; ++i) subset[i] = max(subset[i], tmp[i]);
        }
        
        int i;
        for (const string& a : A) {
            tmp = getCounter(a);
            for (i = 0; i < 26; ++i) {
                if (tmp[i] < subset[i]) break;
            }
            if (i == 26) res.push_back(a);
        }
        return res;
    }
    
    vector<int> getCounter(const string& s) {
        vector<int> res(26);
        for (const char c : s) ++res[c - 'a'];
        return res;
    }
};