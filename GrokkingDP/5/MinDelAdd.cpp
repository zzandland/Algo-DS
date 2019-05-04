#include <iostream>
#include <vector>

std::vector<int> MinDelAddTransform(std::string str1, std::string str2);
void PrintPair(std::vector<int>& pair);

int main(void) {
  std::vector<int> a1 = MinDelAddTransform("abc", "fbc");
  std::vector<int> a2 = MinDelAddTransform("abdca", "cbda");
  std::vector<int> a3 = MinDelAddTransform("passport", "ppsspt");
  PrintPair(a1);
  PrintPair(a2);
  PrintPair(a3);
  return 0;
}

std::vector<int> MinDelAddTransform(std::string str1, std::string str2) {
  int len1 = str1.length();
  int len2 = str2.length();
  std::vector<std::vector<int>> dp(2, std::vector<int>(len2 + 1));
  int max_len = 0;
  for (int i = 0; i < len1; ++i) {
    for (int j = 1; j <= len2; ++j) {
      if (str1[i] == str2[j]) {
        dp[1][j] = dp[0][j - 1] + 1;
        max_len = std::max(max_len, dp[1][j]);
      } else {
        dp[1][j] = std::max(dp[0][j], dp[1][j - 1]);
      }
    }
    for (int k = 1; k <= len2; ++k)
      dp[0][k] = dp[1][k];
  }
  std::vector<int> out = {len1 - max_len, len2 - max_len};
  return out;
}

void PrintPair(std::vector<int>& pair) {
  std::cout << pair[0] << " deletions and " << pair[1] << " additions."
            << std::endl;
}
