class Solution {
public:
    bool hasAllCodes(string s, int k) {
        if (s.length() < pow(2, k)) return false;
        unordered_set<string> left;
        string tmp;
        dfs(tmp, k, left);
        for (int i = 0; i < s.length() - k + 1; ++i) {
            string piece = s.substr(i, k);
            if (left.count(piece)) left.erase(piece);
        }
        return left.empty();
    }
    
    void dfs(string& tmp, int k, unordered_set<string>& left) {
        if (tmp.length() == k) {
            string cpy = tmp;
            left.emplace(cpy);
            return;
        }
        tmp += '0';
        dfs(tmp, k, left);
        tmp.pop_back();
        tmp += '1';
        dfs(tmp, k, left);
        tmp.pop_back();
    }
};