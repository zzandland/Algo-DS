#include <iostream>
#include <vector>

enum class Method { BRUTE_LCS, BRUTE, MEM, BU };

int ShortestCommonSuperseq(std::string seq1, std::string seq2, Method m);
int BruteLCS(std::string seq1, std::string seq2, size_t i1, size_t i2);
int Brute(std::string seq1, std::string seq2, size_t i1, size_t i2);
int Memoize(std::string seq1, std::string seq2, size_t i1, size_t i2,
            std::vector<std::vector<int>>& dp);

int main(void) {
  Method m = Method::BRUTE;
  std::cout << ShortestCommonSuperseq("abcf", "bdcf", m) << ":"
            << ShortestCommonSuperseq("dynamic", "programming", m);
  return 0;
}

int ShortestCommonSuperseq(std::string seq1, std::string seq2, Method m) {
  int longest_subseq;
  switch (m) {
    case Method::BRUTE_LCS:
      longest_subseq = BruteLCS(seq1, seq2, 0, 0);
      return (seq1.length() - longest_subseq) +
             (seq2.length() - longest_subseq) + longest_subseq;
    case Method::BRUTE:
      return Brute(seq1, seq2, 0, 0);
    case Method::MEM:
    case Method::BU:
      return 0;
  }
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
}
