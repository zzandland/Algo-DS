class Solution {
public:
    string customSortString(string order, string str) {
        vector<int> freq(26, 0);
        for (char c : str)
            ++freq[c - 'a'];
        ostringstream res;
        for (char c : order) {
            for (int i = 0; i < freq[c - 'a']; ++i) {
                res << c;
            }
            freq[c - 'a'] = 0;
        }
        for (int i = 0; i < 26; ++i) {
            while (freq[i]-- > 0) {
                res << (char)(i + 'a');
            }
        }
        return res.str();
    }
};