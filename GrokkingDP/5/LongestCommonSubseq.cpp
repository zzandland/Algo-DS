#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

struct Int {
  int val;
};

int LongestCommonSubseq(std::string str1, std::string str2, Method m);
int Brute(std::string str1, std::string str2, size_t i, size_t j);
int Memoize(std::string str1, std::string str2, size_t i, size_t j,
            std::vector<std::vector<Int*>>& dp);
int BU(std::string str1, std::string str2);

int main(void) {
  Method m = Method::BU;
  std::cout << LongestCommonSubseq("abdca", "cbda", m) << ":"
            << LongestCommonSubseq("passport", "ppsspt", m);
  return 0;
}

int LongestCommonSubseq(std::string str1, std::string str2, Method m) {
  std::vector<std::vector<Int*>> dp(str1.length(),
                                    std::vector<Int*>(str2.length()));
  switch (m) {
    case Method::BRUTE:
      return Brute(str1, str2, 0, 0);
    case Method::MEM:
      return Memoize(str1, str2, 0, 0, dp);
    case Method::BU:
      return BU(str1, str2);
  }
}

int Brute(std::string str1, std::string str2, size_t i, size_t j) {
  if (i == str1.length() || j == str2.length()) return 0;
  if (str1[i] == str2[j]) return 1 + Brute(str1, str2, i + 1, j + 1);
  return std::max(Brute(str1, str2, i + 1, j), Brute(str1, str2, i, j + 1));
}

int Memoize(std::string str1, std::string str2, size_t i, size_t j,
            std::vector<std::vector<Int*>>& dp) {
  if (i == str1.length() || j == str2.length()) return 0;
  if (dp[i][j] == nullptr) {
    dp[i][j] = new Int();
    if (str1[i] == str2[j])
      dp[i][j]->val = 1 + Memoize(str1, str2, i + 1, j + 1, dp);
    else
      dp[i][j]->val = std::max(Memoize(str1, str2, i + 1, j, dp),
                               Memoize(str1, str2, i, j + 1, dp));
  }
  return dp[i][j]->val;
}

int BU(std::string str1, std::string str2) {
  int len1 = str1.length();
  int len2 = str2.length();
  std::vector<std::vector<int>> dp(2, std::vector<int>(len2 + 1));
  for (int i = 0; i < len1; ++i) {
    for (int j = 1; j <= len2; ++j) {
      if (str1[i] == str2[j - 1])
        dp[1][j] = dp[0][j - 1] + 1;
      else
        dp[1][j] = std::max(dp[0][j], dp[1][j - 1]);
    }
    for (int k = 1; k <= len2; ++k)
      dp[0][k] = dp[1][k];
  }
  return dp[1][len2];
}
