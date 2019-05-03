#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

struct Int {
  int val;
};

int PalindromicPartition(std::string str, Method m);
int Brute(std::string str, size_t l, size_t r);
int Memoize(std::string str, size_t l, size_t r,
            std::vector<std::vector<Int*>>& dp);
int BU(std::string str);

int main(void) {
  Method m = Method::BU;
  std::cout << PalindromicPartition("abdbca", m) << ":"
            << PalindromicPartition("cddpd", m) << ":"
            << PalindromicPartition("pqr", m) << ":"
            << PalindromicPartition("pp", m) << ":"
            << PalindromicPartition("isnoijsdfnwabdba", m) << ":"
            << PalindromicPartition("isdfnijoiwenriojsidjfabdba", m);
  return 0;
}

int PalindromicPartition(std::string str, Method m) {
  int n = str.length();
  std::vector<std::vector<Int*>> dp(n, std::vector<Int*>(n));
  switch (m) {
    case Method::BRUTE:
      return Brute(str, 0, n - 1);
    case Method::MEM:
      return Memoize(str, 0, n - 1, dp);
    case Method::BU:
      return BU(str);
  }
}

int Brute(std::string str, size_t l, size_t r) {
  if (l >= r) return 0;
  if (str[l] == str[r] && Brute(str, l + 1, r - 1) == 0) return 0;
  return std::min(Brute(str, l + 1, r), Brute(str, l, r - 1)) + 1;
}

int Memoize(std::string str, size_t l, size_t r,
            std::vector<std::vector<Int*>>& dp) {
  if (l >= r) return 0;
  if (dp[l][r] == nullptr) {
    dp[l][r] = new Int();
    if (str[l] == str[r] && Memoize(str, l + 1, r - 1, dp) == 0)
      dp[l][r]->val = 0;
    else
      dp[l][r]->val =
          std::min(Memoize(str, l + 1, r, dp), Memoize(str, l, r - 1, dp)) + 1;
  }
  return dp[l][r]->val;
}

int BU(std::string str) {
  int n = str.length();
  std::vector<std::vector<int>> dp(n, std::vector<int>(n));
  for (int l = n - 2; l >= 0; --l) {
    for (int r = l + 1; r < n; ++r) {
      if (str[l] == str[r] && dp[l + 1][r - 1] == 0)
        dp[l][r] = 0;
      else
        dp[l][r] = std::min(dp[l + 1][r], dp[l][r - 1]) + 1;
    }  
  }
  return dp[0][n - 1];
}
