class Solution {
public:
    bool isIsomorphic(string s, string t) {
        vector<char> A(128, ' ');
        vector<char> B(128, ' ');
        for (int i = 0; i < s.length(); ++i) {
            char a = s[i], b = t[i];
            if (A[a] == ' ' && B[b] == ' ') {
                A[a] = b;
                B[b] = a;
            } else if (A[a] != b || B[b] != a) {
                return false;
            }
        }
        return true;
    }
};