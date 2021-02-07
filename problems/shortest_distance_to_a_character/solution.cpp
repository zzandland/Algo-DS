class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> idx = {-10000};
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == c) idx.push_back(i);
        }
        idx.push_back(10000);
        vector<int> res;
        for (int i = 0, j = 1; i < s.length(); ++i) {
            if (i > idx[j]) j++;
            res.push_back(min(i - idx[j-1], idx[j] - i));
        }
        return res;
    }
};