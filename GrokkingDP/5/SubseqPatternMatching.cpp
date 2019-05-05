#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int SubseqPatternMatching(std::string str, std::string pat, Method m);
int Brute(std::string str, std::string pat, size_t i, size_t j);
int Memoize(std::string str, std::string pat, size_t i, size_t j,
            std::vector<std::vector<int>>& dp);
int BU(std::string str, std::string pat);

int main(void) {
  Method m = Method::BU;
  std::cout << SubseqPatternMatching("baxmx", "ax", m) << ":"
            << SubseqPatternMatching("tomorrow", "tor", m) << ":"
            << SubseqPatternMatching("happyhacking", "hpp", m);
  return 0;
}

int SubseqPatternMatching(std::string str, std::string pat, Method m) {
  std::vector<std::vector<int>> dp(str.length(),
                                   std::vector<int>(pat.length()));
  switch (m) {
    case Method::BRUTE:
      return Brute(str, pat, 0, 0);
    case Method::MEM:
      return Memoize(str, pat, 0, 0, dp);
    case Method::BU:
      return BU(str, pat);
  }
}

int Brute(std::string str, std::string pat, size_t i, size_t j) {
  if (j == pat.length()) return 1;
  if (i == str.length()) return 0;
  int inc = 0;
  if (str[i] == pat[j]) inc = Brute(str, pat, i + 1, j + 1);
  return inc + Brute(str, pat, i + 1, j);
}

int Memoize(std::string str, std::string pat, size_t i, size_t j,
            std::vector<std::vector<int>>& dp) {
  if (j == pat.length()) return 1;
  if (i == str.length()) return 0;
  if (dp[i][j] == 0) {
    int inc = 0;
    if (str[i] == pat[j]) inc = Memoize(str, pat, i + 1, j + 1, dp);
    dp[i][j] = inc + Memoize(str, pat, i + 1, j, dp);
  }
  return dp[i][j];
}

int BU(std::string str, std::string pat) {
  int str_len = str.length();
  int pat_len = pat.length();
  std::vector<std::vector<int>> dp(str_len + 1, std::vector<int>(pat_len + 1));
  for (int i = 0; i <= str_len; ++i)
    dp[i][0] = 1;
  for (int i = 1; i <= str_len; ++i) {
    for (int j = 1; j <= pat_len; ++j) {
      if (pat[j - 1] == str[i - 1]) dp[i][j] = dp[i - 1][j - 1];
      dp[i][j] += dp[i - 1][j];
    }
  }
  return dp[str_len][pat_len];
}
