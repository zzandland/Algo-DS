class Solution {
public:
    int countBinarySubstrings(string s) {
        char prev = '2';
        int cnt = 0;
        vector<int> cnts;
        for (char c : s) {
            if (prev != c) {
                cnts.push_back(cnt);
                prev = c;
                cnt = 1;
            } else {
                ++cnt;
            }
        }
        cnts.push_back(cnt);
        int res = 0;
        for (int i = 0; i < cnts.size() - 1; ++i)
            res += min(cnts[i], cnts[i+1]);
        return res;
    }
};