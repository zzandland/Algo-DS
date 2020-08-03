class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size()-1;
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        while (l < r) {
            if (!isalnum(s[l])) ++l;
            else if (!isalnum(s[r])) --r;
            else if (s[l++] != s[r--]) return false;
        }
        return true;
    }
};