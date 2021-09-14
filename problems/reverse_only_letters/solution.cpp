class Solution {
public:
    string reverseOnlyLetters(string s) {
        vector<char> res(s.length(), ' ');
        for (int i = 0; i < s.length(); ++i) {
            if (!isalpha(s[i])) {
                res[i] = s[i];
            }
        }
        int j = s.length() - 1;
        for (int i = 0; i < res.size(); ++i) {
            if (res[i] != ' ') {
                continue;
            }
            while (!isalpha(s[j])) {--j;}
            res[i] = s[j--];
        }
        return string(res.begin(), res.end());
    }
};