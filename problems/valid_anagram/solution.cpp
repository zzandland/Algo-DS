class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> a;
        unordered_map<char, int> b;
        for (int i = 0; i < s.length(); ++i) {
            a[s[i] - 'a']++;
            b[t[i] - 'a']++;
        }
        for (const auto &[k, v] : a) if (v != b[k]) return false;
        for (const auto &[k, v] : b) if (v != a[k]) return false;
        return true;
    }
};