#include <iostream>
#include <vector>

enum class Method {
  BRUTE, BU
};

int CountPalindromicSubstr(std::string str, Method m);
int Brute(std::string str, size_t start, size_t end);
int BU(std::string str);

int main(void)
{
  Method m = Method::BU;
  std::cout << CountPalindromicSubstr("abdbca", m) << ":"
            << CountPalindromicSubstr("cddpd", m) << ":"
            << CountPalindromicSubstr("pqr", m);
  return 0;
}

int CountPalindromicSubstr(std::string str, Method m) {
  switch (m) {
    case Method::BRUTE:
      return Brute(str, 0, str.length() - 1);
    case Method::BU:
      return BU(str);
  }
}

int Brute(std::string str, size_t start, size_t end) {
  if (str[start] == str[end]) return 1;
  if (start > end) return 0;
  int expand = 0;
  return expand + Brute(str, start + 1, end) + Brute(str, start, end - 1);
}

int BU(std::string str) {
  int n = str.length();
  std::vector<std::vector<bool>> dp(n, std::vector<bool>(n));
  int count = 0;
  for (int i = 0; i < n; ++i) {
    dp[i][i] = true;
    ++count;
  }
  for (int l = n - 1; l >= 0; --l) {
    for (int r = l + 1; r < n; ++r) {
      if (str[l] == str[r] && (dp[l + 1][r - 1] || r - l == 1)) {
        dp[l][r] = true;
        ++count;
      }
    }
  }
  return count;
}
