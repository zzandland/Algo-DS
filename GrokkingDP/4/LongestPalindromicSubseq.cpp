#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int LongestPalindromicSubseq(std::string seq, Method m);
int Brute(std::string seq, size_t left, size_t right);
int Memoize(std::string seq, size_t left, size_t right,
            std::vector<std::vector<int>>& dp);
int BU(std::string seq, std::vector<std::vector<int>>& dp);
bool CheckPalindrome(std::string str);

int main(void) {
  Method m = Method::MEM;
  std::cout << LongestPalindromicSubseq("abdbca", m) << ":"
            << LongestPalindromicSubseq("cddpd", m) << ":"
            << LongestPalindromicSubseq("pqdjsdfiwneriwejrnsdijifsdnerwdsnifnwoeirjeiwrr", m);
  return 0;
}

int LongestPalindromicSubseq(std::string seq, Method m) {
  std::vector<std::vector<int>> dp(seq.length(), std::vector<int>(seq.length()));
  switch (m) {
    case Method::BRUTE:
      return Brute(seq, 0, seq.length() - 1);
    case Method::MEM:
      return Memoize(seq, 0, seq.length() - 1, dp);
    case Method::BU:
      return BU(seq, dp);
  }
}

int Brute(std::string seq, size_t left, size_t right) {
  if (left == right) return 1;
  if (left > right) return 0;
  if (seq[left] == seq[right]) return 2 + Brute(seq, left + 1, right - 1);
  return std::max(Brute(seq, left + 1, right), Brute(seq, left, right - 1));
}

int Memoize(std::string seq, size_t left, size_t right,
            std::vector<std::vector<int>>& dp) {
  if (left == right) return 1;
  if (left > right) return 0;
  if (dp[left][right] == 0) {
    if (seq[left] == seq[right])
      dp[left][right] = 2 + Memoize(seq, left + 1, right - 1, dp);
    else
      dp[left][right] = std::max(Memoize(seq, left + 1, right, dp),
                                 Memoize(seq, left, right - 1, dp));
  }
  return dp[left][right];
}

int BU(std::string seq, std::vector<std::vector<int>>& dp) {
  for (size_t i = 0; i < seq.length(); ++i)
    dp[i][i] = 1;
  for (int l = seq.length() - 2; l >= 0; --l) {
    for (size_t r = l + 1; r < seq.length(); ++r) {
      if (seq[l] == seq[r]) dp[l][r] = 2 + dp[l + 1][r - 1];
      else dp[l][r] = std::max(dp[l + 1][r], dp[l][r - 1]);
    }
  }
  return dp[0][seq.length() - 1];
}
