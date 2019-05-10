class Solution {
public:
  string intToRoman(int num) {
    vector<int> nums = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> letters = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int i = 0;
    string output = "";
    while (i < (int)nums.size() && num > 0) {
      if (num >= nums[i]) {
        output += letters[i];
        num -= nums[i];
      } else {
        ++i;
      }
    }
    return output;
  }
};