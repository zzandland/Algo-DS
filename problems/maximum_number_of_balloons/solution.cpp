class Solution {
public:
    int maxNumberOfBalloons(string text) {
        vector<int> freqs(27, 0);
        for (char c : text) {
            ++freqs[c - 'a'];
        }
        vector<char> balloon{'b', 'a', 'l', 'o', 'n'};
        int res = INT_MAX;
        for (char c : balloon) {
            int pos = c - 'a';
            int cnt = (c == 'l' || c == 'o') ? freqs[pos] / 2 : freqs[pos];
            res = min(res, cnt);
        }
        return res;
    }
};