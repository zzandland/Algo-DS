class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        string res = "";
        for (string t : d) {
            int i = 0;
            for (int j = 0; i < t.length() && j < s.length(); ++j) {
                if (t[i] == s[j]) ++i;
            }
            if (i == t.length()) {
                if (res.length() < t.length()) res = t;
                else if (res.length() == t.length() && t.compare(res) < 0) res = t;
            }
        }
        return res;
    }
};