class Solution {
public:
    int romanToInt(string s) {
        int res = 0;
        unordered_map<char, int> d = { {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000} };
        for (char c : s) res += d[c];
        for (int i = 0; i < s.length()-1; ++i) {
            string ss = s.substr(i, 2);
            if (ss == "IV" || ss == "IX") res -= 2;
            else if (ss == "XL" || ss == "XC") res -= 20;
            else if (ss == "CD" || ss == "CM") res -= 200;
        }
        return res;
    }
};