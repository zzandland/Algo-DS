#include <iostream>
#include <map>

int CountEval(const std::string& s, bool result, std::map<std::string, int>& dp) {
  int s_len = s.length();
  if (s_len == 0) return 0;
  if (s_len == 1) return (s[0] - '0' == result) ? 1 : 0;

  char b = result + '0';
  std::string key = s + b;

  if (dp.find(key) == dp.end()) {
    int ways = 0;
    for (int i = 1; i < s_len; i += 2) {
      char c = s[i];
      std::string left = s.substr(0, i);
      std::string right = s.substr(i + 1);

      int left_true = CountEval(left, true, dp);
      int left_false = CountEval(left, false, dp);
      int right_true = CountEval(right, true, dp);
      int right_false = CountEval(right, false, dp);
      int total = (left_true + left_false) * (right_true + right_false);
      int total_true;

      switch (c) {
        case '^':
          total_true = left_true * right_false + left_false * right_true;
          break;
        case '&':
          total_true = left_true * right_true;
          break;
        case '|':
          total_true = left_true * right_true
            + left_false * right_true
            + left_true * right_false;
          break;
      }

      int sub_ways = (result) ? total_true : total - total_true;
      ways += sub_ways;
    }
    dp[key] = ways;
  }
  return dp[key];
}

int main(void)
{
  std::string s = "0&0&0&1^1|0";
  std::map<std::string, int> dp;
  std::cout << CountEval(s, true, dp);
  return 0;
}
