#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int LongestRepeatingSubseq(std::string str, Method m);
int Brute(std::string str, size_t i, size_t j);
int Memoize(std::string str, size_t i, size_t j,
            std::vector<std::vector<int>>& dp);
int BU(std::string str);

int main(void) {
  Method m = Method::MEM;
  std::cout << LongestRepeatingSubseq("tomorrow", m) << ":"
            << LongestRepeatingSubseq("aabdbcec", m) << ":"
            << LongestRepeatingSubseq("fmff", m) << ":"
            << LongestRepeatingSubseq("fmffnaijsdfnwer", m);
  return 0;
}

int LongestRepeatingSubseq(std::string str, Method m) {
  std::vector<std::vector<int>> dp(str.length(),
                                   std::vector<int>(str.length()));
  switch (m) {
    case Method::BRUTE:
      return Brute(str, 1, 0);
    case Method::MEM:
      return Memoize(str, 1, 0, dp);
    case Method::BU:
      return BU(str);
  }
}

int Brute(std::string str, size_t i, size_t j) {
  if (j >= i || i == str.length()) return 0;
  if (str[i] == str[j]) return 1 + Brute(str, i + 1, j + 1);
  return std::max(Brute(str, i + 1, j), Brute(str, i, j + 1));
}

int Memoize(std::string str, size_t i, size_t j,
            std::vector<std::vector<int>>& dp) {
  if (j >= i || i == str.length()) return 0;
  if (dp[i][j] == 0) {
    if (str[i] == str[j])
      dp[i][j] = 1 + Brute(str, i + 1, j + 1);
    else
      dp[i][j] = std::max(Brute(str, i + 1, j), Brute(str, i, j + 1));
  }
  return dp[i][j];
}

int BU(std::string str) {
  int len = str.length();
  std::vector<std::vector<int>> dp(len + 1,
                                   std::vector<int>(len + 1));
  int longest = 0;
  for (int i = 1; i <= len; ++i) {
    for (int j = i + 1; j <= len; ++j) {
      if (str[i - 1] == str[j - 1])
        dp[i][j] = dp[i - 1][j - 1] + 1;
      else
        dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
    }
    longest = std::max(longest, dp[i][len]);
  }
  return longest;
}
