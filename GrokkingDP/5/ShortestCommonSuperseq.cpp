#include <iostream>
#include <vector>

enum class Method { BRUTE_LCS, BRUTE, MEM, BU };

int ShortestCommonSuperseq(std::string seq1, std::string seq2, Method m);
int BruteLCS(std::string seq1, std::string seq2, size_t i1, size_t i2);
int Brute(std::string seq1, std::string seq2, size_t i1, size_t i2);
int Memoize(std::string seq1, std::string seq2, size_t i1, size_t i2,
            std::vector<std::vector<int>>& dp);
int BU(std::string seq1, std::string seq2);

int main(void) {
  Method m = Method::BU;
  std::cout << ShortestCommonSuperseq("abcf", "bdcf", m) << ":"
            << ShortestCommonSuperseq("dynamic", "programming", m);
  return 0;
}

int ShortestCommonSuperseq(std::string seq1, std::string seq2, Method m) {
  int longest_subseq;
  std::vector<std::vector<int>> dp(seq1.length(), std::vector<int>(seq2.length()));
  switch (m) {
    case Method::BRUTE_LCS:
      longest_subseq = BruteLCS(seq1, seq2, 0, 0);
      return (seq1.length() - longest_subseq) +
             (seq2.length() - longest_subseq) + longest_subseq;
    case Method::BRUTE:
      return Brute(seq1, seq2, 0, 0);
    case Method::MEM:
      return Memoize(seq1, seq2, 0, 0, dp);
    case Method::BU:
      return BU(seq1, seq2);
  }
  return 0;
}

int BruteLCS(std::string seq1, std::string seq2, size_t i1, size_t i2) {
  if (i1 == seq1.length() || i2 == seq2.length()) return 0;
  if (seq1[i1] == seq2[i2]) return 1 + BruteLCS(seq1, seq2, i1 + 1, i2 + 1);
  return std::max(BruteLCS(seq1, seq2, i1 + 1, i2),
                  BruteLCS(seq1, seq2, i1, i2 + 1));
}

int Brute(std::string seq1, std::string seq2, size_t i1, size_t i2) {
  if (i1 == seq1.length() || i2 == seq2.length())
    return std::max(seq1.length() - i1, seq2.length() - i2);
  if (seq1[i1] == seq2[i2]) return 1 + Brute(seq1, seq2, i1 + 1, i2 + 1);
  return 1 +
         std::min(Brute(seq1, seq2, i1 + 1, i2), Brute(seq1, seq2, i1, i2 + 1));
};

int Memoize(std::string seq1, std::string seq2, size_t i1, size_t i2,
            std::vector<std::vector<int>>& dp) {
  if (i1 == seq1.length() || i2 == seq2.length())
    return std::max(seq1.length() - i1, seq2.length() - i2);
  if (dp[i1][i2] == 0) {
    if (seq1[i1] == seq2[i2])
      return 1 + Memoize(seq1, seq2, i1 + 1, i2 + 1, dp);
    return 1 + std::min(Memoize(seq1, seq2, i1 + 1, i2, dp),
                        Memoize(seq1, seq2, i1, i2 + 1, dp));
  }
  return dp[i1][i2];
}

int BU(std::string seq1, std::string seq2) {
  int len1 = seq1.size();
  int len2 = seq2.size();
  std::vector<std::vector<int>> dp(2, std::vector<int>(len1 + 1));
  for (int i = 1; i <= len1 + 1; ++i)
    dp[0][i - 1] = i - 1;
  for (int i = 0; i < len2; ++i) {
    dp[1][0] = i + 1;
    for (int j = 1; j <= len1; ++j) {
      if (seq1[j - 1] == seq2[i])
        dp[1][j] = dp[0][j - 1] + 1;
      else
        dp[1][j] = 1 + std::min(dp[0][j], dp[1][j - 1]);
    }
    for (int k = 0; k <= len1; ++k)
      dp[0][k] = dp[1][k];
  }
  return dp[1][len1];
}
