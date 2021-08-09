class Solution {
public:
    string addStrings(string num1, string num2) {
        stringstream oss;
        int overflow = 0;
        for (int a = num1.length() - 1, b = num2.length() - 1; a >= 0 || b >= 0; --a, --b) {
            int aVal = a >= 0 ? num1[a] - '0' : 0;
            int bVal = b >= 0 ? num2[b] - '0' : 0;
            oss << (aVal + bVal + overflow) % 10;
            overflow = (aVal + bVal + overflow) / 10;
        }
        if (overflow == 1) oss << 1;
        string res = oss.str();
        reverse(res.begin(), res.end());
        return res;
    }
};