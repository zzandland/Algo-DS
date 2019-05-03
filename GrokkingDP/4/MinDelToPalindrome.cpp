#include <iostream>
#include <vector>

int MinDelToPalindrome(std::string str);

int main(void)
{
  std::cout << MinDelToPalindrome("abdcba") << ":"
            << MinDelToPalindrome("cddpd") << ":"
            << MinDelToPalindrome("pqr");
  return 0;
}

int MinDelToPalindrome(std::string str) {
  int n = str.length();
  std::vector<std::vector<int>> dp(n, std::vector<int>(n));
  for (int i = 0; i < n; ++i)
    dp[i][i] = 1;
  for (int l = n - 2; l >= 0; --l) {
    for (int r = l + 1; r < n; ++r) {
      int match = 0;
      if (str[l] == str[r]) match = dp[l + 1][r - 1] + 2;
      dp[l][r] = std::max(match, std::max(dp[l + 1][r], dp[l][r - 1]));
    }
  }
  return n - dp[0][n - 1];
}
