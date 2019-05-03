#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int LPS(std::string str, Method m);
int Brute(std::string str, size_t start, size_t end);
int Memoize(std::string str, size_t start, size_t end, std::vector<std::vector<int>>& dp);
int BU(std::string str);
int BUBool(std::string str);

int main(void) {
  Method m = Method::BU;
  std::cout << LPS("abdbca", m) << ":"
            << LPS("cddpd", m) << ":"
            << LPS("pqridjfnierabcdefedcbafjssdjfwiejfewnkfddifjiejrn", m);
  return 0;
}

int LPS(std::string str, Method m) {
  std::vector<std::vector<int>> dp(str.length(), std::vector<int>(str.length()));
  switch (m) {
    case Method::BRUTE:
      return Brute(str, 0, str.length() - 1);
    case Method::MEM:
      return Memoize(str, 0, str.length() - 1, dp);
    case Method::BU:
      return BUBool(str);
  }
}

int Brute(std::string str, size_t start, size_t end) {
  if (start > end) return 0;
  if (start == end) return 1;
  int c1 = 0;
  if (str[start] == str[end]) {
    int remain_len = end - start - 1;
    if (remain_len == Brute(str, start + 1, end - 1))
      c1 = remain_len + 2;
  }
  int c2 = Brute(str, start + 1, end);
  int c3 = Brute(str, start, end - 1);
  return std::max(c1, std::max(c2, c3));
}

int Memoize(std::string str, size_t start, size_t end, std::vector<std::vector<int>>& dp) {
  if (start > end) return 0;
  if (start == end) return 1;
  if (dp[start][end] == 0) {
    int c1 = 0;
    if (str[start] == str[end]) {
      int remain_len = end - start - 1;
      if (remain_len == Brute(str, start + 1, end - 1))
        c1 = remain_len + 2;
    }
    int c2 = Brute(str, start + 1, end);
    int c3 = Brute(str, start, end - 1);
    dp[start][end] = std::max(c1, std::max(c2, c3));
  }
  return dp[start][end];
}

int BU(std::string str) {
  int n = str.length();
  std::vector<std::vector<int>> dp(n, std::vector<int>(n));
  for (int i = 0; i < n; ++i)
    dp[i][i] = 1;
  for (int l = n - 2; l >= 0; --l) {
    for (int r = l + 1; r < n; ++r) {
      if (str[l] == str[r] && r - l - 1 == dp[l + 1][r - 1])
        dp[l][r] = dp[l + 1][r - 1] + 2;
      else
        dp[l][r] = std::max(dp[l + 1][r], dp[l][r - 1]);
    }
  }
  return dp[0][n - 1];
}

int BUBool(std::string str) {
  int n = str.length();
  std::vector<std::vector<bool>> dp(n, std::vector<bool>(n));
  for (int i = 0; i < n; ++i)
    dp[i][i] = true;
  int longest = 0;
  for (int l = n - 2; l >= 0; --l) {
    for (int r = l + 1; r < n; ++r) {
      if (str[l] == str[r] && (dp[l + 1][r - 1] || r - l == 1)) {
        dp[l][r] = true;
        longest = std::max(longest, r - l + 1);
      }
    }
  }
  return longest;
}
