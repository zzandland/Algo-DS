#include <iostream>
#include <vector>

enum class Method {
  BRUTE, BU
};

int MaxRibbonCut(std::vector<int>& lengths, int n, Method m);
int Brute(std::vector<int>& lengths, int n, size_t i);
int BU(std::vector<int>& lengths, int n, std::vector<std::vector<int>>& dp);

int main(void)
{
  Method m = Method::BRUTE;  
  std::vector<int> len1 = {2, 3, 5};
  std::vector<int> len2 = {2, 3};
  std::vector<int> len3 = {3, 5, 7};
  std::cout << MaxRibbonCut(len1, 5, m) << ":"
            << MaxRibbonCut(len2, 7, m) << ":"
            << MaxRibbonCut(len3, 4958, m);
  return 0;
};

int MaxRibbonCut(std::vector<int>& lengths, int n, Method m) {
  switch (m) {
    case Method::BRUTE:
      return Brute(lengths, n, 0);
    case Method::BU:
      std::vector<std::vector<int>> dp(lengths.size(), std::vector<int>(n + 1));
      return BU(lengths, n, dp);
  }
};

int Brute(std::vector<int>& lengths, int n, size_t i) {
  if (n == 0) return 0;  
  if (n < 0 || i == lengths.size()) return -1;
  int len1 = -1;
  if (n >= lengths[i]) {
    int tmp = Brute(lengths, n - lengths[i], i);  
    if (tmp != -1)
      len1 = 1 + tmp;
  }
  return std::max(len1, Brute(lengths, n, i + 1));
};

int BU(std::vector<int>& lengths, int n, std::vector<std::vector<int>>& dp) {
  for (size_t i = 0; i < lengths.size(); ++i) {
    for (int s = 1; s <= n; ++s) {
      if (i > 0) {
        if (s >= lengths[i])
          dp[i][s] = std::max(dp[i - 1][s], dp[i][s - lengths[i]]); 
        else
          dp[i][s] = dp[i - 1][s];
      } else {
        dp[i][s] = s / lengths[i];
      }
    }
  }
  return dp[lengths.size() - 1][n];
}
