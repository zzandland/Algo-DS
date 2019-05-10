#include <climits>

class Solution {
public:
  int myAtoi(string str) {
    int i = 0;
    int sign = 1;
    int output = 0;
    while (str[i] == ' ') ++i;
    if (str[i] == '-' || str[i] == '+') {
      sign = (str[i] == '-') ? -1 : 1;
      ++i;
    }
    for (; i < (int)str.length(); ++i) {
      int c = str[i];  
      bool is_num = (c >= 48 && c < 58);
      if (!is_num) break;
      if (INT_MAX / 10 < output)
        return (sign == 1) ? INT_MAX : INT_MIN;
      output *= 10;
      int c_val = c - 48;
      if (INT_MAX - c_val < output)
        return (sign == 1) ? INT_MAX : INT_MIN;
      output += c_val;
    }
    return output * sign;
  }
};