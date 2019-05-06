#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int LongestAlternatingSubseq(std::vector<int>& nums, Method m);
int Brute(std::vector<int>& nums, int i, int j, bool is_asc);
int Memoize(std::vector<int>& nums, int i, int j, bool is_asc,
            std::vector<std::vector<std::vector<int>>>& dp);
int BU(std::vector<int>& nums);

int main(void) {
  std::vector<int> n1 = {1, 2, 3, 4};
  std::vector<int> n2 = {3, 2, 1, 4};
  std::vector<int> n3 = {1, 3, 2, 4};
  Method m = Method::BU;
  std::cout << LongestAlternatingSubseq(n1, m) << ":"
            << LongestAlternatingSubseq(n2, m) << ":"
            << LongestAlternatingSubseq(n3, m);
  return 0;
}

int LongestAlternatingSubseq(std::vector<int>& nums, Method m) {
  int n = nums.size();
  std::vector<std::vector<std::vector<int>>> dp(
      n, std::vector<std::vector<int>>(n, std::vector<int>(2)));
  switch (m) {
    case Method::BRUTE:
      return std::max(Brute(nums, 1, 0, true), Brute(nums, 1, 0, false)) + 1;
    case Method::MEM:
      return std::max(Memoize(nums, 1, 0, true, dp),
                      Memoize(nums, 1, 0, false, dp)) +
             1;
    case Method::BU:
      return BU(nums);
  }
}

int Brute(std::vector<int>& nums, int i, int j, bool is_asc) {
  if (i == (int)nums.size()) return 0;
  int c1 = 0;
  if (is_asc) {
    if (nums[i] > nums[j]) c1 = 1 + Brute(nums, i + 1, i, !is_asc);
  } else {
    if (nums[i] < nums[j]) c1 = 1 + Brute(nums, i + 1, j, !is_asc);
  }
  int c2 = Brute(nums, i + 1, j, is_asc);
  return std::max(c1, c2);
}

int Memoize(std::vector<int>& nums, int i, int j, bool is_asc,
            std::vector<std::vector<std::vector<int>>>& dp) {
  if (i == (int)nums.size()) return 0;
  if (dp[i][j + 1][(int)is_asc + 1] == 0) {
    int c1 = 0;
    if (is_asc) {
      if (nums[i] > nums[j]) c1 = 1 + Memoize(nums, i + 1, i, !is_asc, dp);
    } else {
      if (nums[i] < nums[j]) c1 = 1 + Memoize(nums, i + 1, i, !is_asc, dp);
    }
    int c2 = Memoize(nums, i + 1, j, is_asc, dp);
    dp[i][j + 1][(int)is_asc + 1] = std::max(c1, c2);
  }
  return dp[i][j + 1][(int)is_asc + 1];
}

int BU(std::vector<int>& nums) {
  int n = nums.size();
  int longest = 1;
  std::vector<std::vector<int>> dp(2, std::vector<int>(n, 1));
  for (int i = 1; i < n; ++i) {
    for (int j = 0; j < i; ++j) {
      if (nums[i] > nums[j])
        dp[0][i] = std::max(dp[0][i], 1 + dp[1][j]);
      else
        dp[1][i] = std::max(dp[1][i], 1 + dp[0][j]);
    }
    longest = std::max(longest, std::max(dp[0][i], dp[1][i]));
  }

  return longest;
}
