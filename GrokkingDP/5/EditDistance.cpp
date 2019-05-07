#include <climits>
#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int EditDistance(std::string str1, std::string str2, Method m);
int Brute(std::string str1, std::string str2, size_t i1, size_t i2);
int Memoize(std::string str1, std::string str2, size_t i1, size_t i2,
            std::vector<std::vector<int>>& dp);
int BU(std::string str1, std::string str2);

int main(void) {
  Method m = Method::BRUTE;
  std::cout << EditDistance("bat", "but", m) << ":"
            << EditDistance("abdca", "cbda", m) << ":"
            << EditDistance("passpot", "ppsspqrt", m) << ":"
            << EditDistance("sdijfnweijf", "sdjifnwes", m);
  return 0;
}

int EditDistance(std::string str1, std::string str2, Method m) {
  std::vector<std::vector<int>> dp(str1.length(),
                                   std::vector<int>(str2.length()));
  switch (m) {
    case Method::BRUTE:
      return Brute(str1, str2, 0, 0);
    case Method::MEM:
      return Memoize(str1, str2, 0, 0, dp);
    case Method::BU:
      return BU(str1, str2);
  }
}

int Brute(std::string str1, std::string str2, size_t i1, size_t i2) {
  if (i1 == str1.length() || i2 == str2.length())
    return std::max(str1.length() - i1, str2.length() - i2);
  if (str1[i1] == str2[i2]) return Brute(str1, str2, i1 + 1, i2 + 1);
  int c1 = 1 + Brute(str1, str2, i1 + 1, i2 + 1);
  int c2 = 1 + Brute(str1, str2, i1 + 1, i2);
  int c3 = 1 + Brute(str1, str2, i1, i2 + 1);
  return std::min(c1, std::min(c2, c3));
}

int Memoize(std::string str1, std::string str2, size_t i1, size_t i2,
            std::vector<std::vector<int>>& dp) {
  if (i1 == str1.length() || i2 == str2.length())
    return std::max(str1.length() - i1, str2.length() - i2);
  if (dp[i1][i2] == 0) {
    if (str1[i1] == str2[i2]) {
      dp[i1][i2] = Memoize(str1, str2, i1 + 1, i2 + 1, dp);
    } else {
      int c1 = 1 + Memoize(str1, str2, i1 + 1, i2 + 1, dp);
      int c2 = 1 + Memoize(str1, str2, i1 + 1, i2, dp);
      int c3 = 1 + Memoize(str1, str2, i1, i2 + 1, dp);
      dp[i1][i2] = std::min(c1, std::min(c2, c3));
    }
  }
  return dp[i1][i2];
}

int BU(std::string str1, std::string str2) {
  int len1 = str1.length();
  int len2 = str2.length();
  std::vector<std::vector<int>> dp(len1 + 1, std::vector<int>(len2 + 1));
  for (int i = 1; i <= len1; ++i)
    dp[i][0] = i;
  for (int j = 1; j <= len2; ++j)
    dp[0][j] = j;
  for (int i = 1; i <= len1; ++i) {
    for (int j = 1; j <= len2; ++j) {
      if (str1[i - 1] == str2[j - 1])
        dp[i][j] = dp[i - 1][j - 1];
      else
        dp[i][j] = 1 + std::min(dp[i - 1][j - 1], std::min(dp[i - 1][j], dp[i][j - 1]));
    }
  }
  return dp[len1][len2];
}
