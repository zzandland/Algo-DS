#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

struct Int {
  int val;
};

int LongestCommonSubstr(std::string str1, std::string str2, Method m);
int Brute(std::string str1, std::string str2, size_t i, size_t j, int curr);
int Memoize(std::string str1, std::string str2, size_t i, size_t j, int curr,
            std::vector<std::vector<std::vector<Int*>>>& dp);
int BU(std::string str1, std::string str2);

int main(void) {
  Method m = Method::BU;
  std::cout << LongestCommonSubstr("abdca", "cbda", m) << ":"
            << LongestCommonSubstr("passport", "ppsspt", m) << ":"
            << LongestCommonSubstr("osndijreswli", "owsjeraoisdn", m);
  return 0;
}

int LongestCommonSubstr(std::string str1, std::string str2, Method m) {
  int max_len = std::max(str1.length(), str2.length());
  std::vector<std::vector<std::vector<Int*>>> dp(
      str1.length(), std::vector<std::vector<Int*>>(
                         str2.length(), std::vector<Int*>(max_len + 1)));
  switch (m) {
    case Method::BRUTE:
      return Brute(str1, str2, 0, 0, 0);
    case Method::MEM:
      return Memoize(str1, str2, 0, 0, 0, dp);
    case Method::BU:
      return BU(str1, str2);
  }
  return 0;
}

int Brute(std::string str1, std::string str2, size_t i, size_t j, int curr) {
  if (i == str1.length() || j == str2.length()) return curr;
  if (str1[i] == str2[j]) curr = Brute(str1, str2, i + 1, j + 1, curr + 1);
  int c1 = Brute(str1, str2, i + 1, j, 0);
  int c2 = Brute(str1, str2, i, j + 1, 0);
  return std::max(curr, std::max(c1, c2));
}

int Memoize(std::string str1, std::string str2, size_t i, size_t j, int curr,
            std::vector<std::vector<std::vector<Int*>>>& dp) {
  if (i == str1.length() || j == str2.length()) return curr;
  if (dp[i][j][curr] == nullptr) {
    dp[i][j][curr] = new Int();
    int c1 = curr;
    if (str1[i] == str2[j]) c1 = Memoize(str1, str2, i + 1, j + 1, curr + 1, dp);
    int c2 = Memoize(str1, str2, i + 1, j, 0, dp);
    int c3 = Memoize(str1, str2, i, j + 1, 0, dp);
    dp[i][j][curr]->val = std::max(c1, std::max(c2, c3));
  }
  return dp[i][j][curr]->val;
}

int BU(std::string str1, std::string str2) {
  int len1 = str1.length() + 1;
  int len2 = str2.length() + 1;
  int max_len = 0;
  std::vector<std::vector<int>> dp(len1, std::vector<int>(len2));
  for (int i = 1; i < len1; ++i) {
    for (int j = 1; j < len2; ++j) {
      if (str1[i] == str2[j]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
        max_len = std::max(max_len, dp[i][j]);
      }
    }
  }
  return max_len;
}
