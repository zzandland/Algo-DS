class Solution {
public:
  int romanToInt(string s) {
    map<char, int> dic = {
      {'I', 1},
      {'V', 5},
      {'X', 10},
      {'L', 50},
      {'C', 100},
      {'D', 500},
      {'M', 1000}
    };
    int sum = 0;
    for (size_t i = 0; i < s.length(); ++i) {
      sum += dic[s[i]];
    }
    
    if (s.find("IV") != string::npos || s.find("IX") != string::npos) sum -= 2;
    if (s.find("XL") != string::npos || s.find("XC") != string::npos) sum -= 20;
    if (s.find("CD") != string::npos || s.find("CM") != string::npos) sum -= 200;

    return sum;
  }
};