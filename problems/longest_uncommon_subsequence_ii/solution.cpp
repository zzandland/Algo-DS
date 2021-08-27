class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        sort(strs.begin(), strs.end(), [&](string &a, string &b) {
            return a.length() > b.length();
        });
        unordered_set<string> seen;
        unordered_map<string, int> freqs;
        for (string s : strs) ++freqs[s];
        string tmp;
        for (auto s : strs) {
            if (freqs[s] == 1 && !seen.count(s)) return s.length();
            explore(0, tmp, s, seen);
        }
        return -1;
    }
    
    void explore(int i, string &tmp, string &s, unordered_set<string>& seen) {
        if (i == s.length()) {
            seen.insert(tmp);
            return;
        }
        tmp.push_back(s[i]);
        explore(i + 1, tmp, s, seen);
        tmp.pop_back();
        explore(i + 1, tmp, s, seen);
    }
};