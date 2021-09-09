class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        long N = shifts.size(), shift = 0;
        stringstream ss;
        for (int i = N - 1; i >= 0; --i) {
            shift += shifts[i] % 26;
            ss << (char)((((s[i] - 'a') + shift) % 26) + 'a');
        }
        string res = ss.str();
        reverse(res.begin(), res.end());
        return res;
    }
};