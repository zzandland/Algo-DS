class Solution {
public:
    string intToRoman(int num) {
        string res;
        helper(num, res, 1000, "M");
        helper(num, res, 900, "CM");
        helper(num, res, 500, "D");
        helper(num, res, 400, "CD");
        helper(num, res, 100, "C");
        helper(num, res, 90, "XC");
        helper(num, res, 50, "L");
        helper(num, res, 40, "XL");
        helper(num, res, 10, "X");
        helper(num, res, 9, "IX");
        helper(num, res, 5, "V");
        helper(num, res, 4, "IV");
        helper(num, res, 1, "I");
        return res;
    }
    
    string helper(int& num, string& res, int val, string add) {
        while (num >= val) {
            num -= val;
            res += add;
        }
        return res;
    }
};