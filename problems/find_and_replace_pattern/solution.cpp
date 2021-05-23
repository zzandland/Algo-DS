class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> res;
        for (const string &w : words) {
            vector<char> map(26, ' ');
            vector<bool> seen(26, false);
            int i = 0;
            for (; i < w.length(); ++i) {
                char a = w[i], b = pattern[i];
                if (map[a - 'a'] == ' ') {
                    if (seen[b - 'a']) break;
                    seen[b - 'a'] = true;
                    map[a - 'a'] = b;
                } else if (map[a - 'a'] != b) {
                    break;
                }
            }
            if (i == w.length()) res.push_back(w);
        }
        return res;
    }
};