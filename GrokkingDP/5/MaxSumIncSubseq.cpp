#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int MaxSumIncSubseq(std::vector<int>& nums, Method m);
int Brute(std::vector<int>& nums, int i, int j);
int Memoize(std::vector<int>& nums, int i, int j,
            std::vector<std::vector<int>>& dp);
int BU(std::vector<int>& nums);

int main(void) {
  std::vector<int> s1 = {4, 1, 2, 6, 10, 1, 12};
  std::vector<int> s2 = {-4, 10, 3, 7, 15};
  Method m = Method::BU;
  std::cout << MaxSumIncSubseq(s1, m) << ":" << MaxSumIncSubseq(s2, m);
  return 0;
}

int MaxSumIncSubseq(std::vector<int>& nums, Method m) {
  std::vector<std::vector<int>> dp(nums.size(), std::vector<int>(nums.size()));
  switch (m) {
    case Method::BRUTE:
      return Brute(nums, 0, -1);
    case Method::MEM:
      return Memoize(nums, 0, -1, dp);
    case Method::BU:
      return BU(nums);
  }
}

int Brute(std::vector<int>& nums, int i, int j) {
  if (i == (int)nums.size()) return 0;
  int include = 0;
  if (j == -1 || nums[i] > nums[j]) include = nums[i] + Brute(nums, i + 1, i);
  return std::max(include, Brute(nums, i + 1, j));
}

int Memoize(std::vector<int>& nums, int i, int j,
            std::vector<std::vector<int>>& dp) {
  if (i == (int)nums.size()) return 0;
  if (dp[i][j + 1] == 0) {
    int include = 0;
    if (j == -1 || nums[i] > nums[j])
      include = nums[i] + Memoize(nums, i + 1, i, dp);
    dp[i][j + 1] = std::max(include, Memoize(nums, i + 1, j, dp));
  }
  return dp[i][j + 1];
}

int BU(std::vector<int>& nums) {
  std::vector<int> dp(nums.size());
  int n = nums.size();
  int largest = 0;
  for (int i = 0; i < n; ++i) {
    dp[i] = nums[i];
    largest = std::max(largest, nums[i]);
  }

  for (int j = 1; j < n; ++j) {
    for (int k = 0; k < j; ++k) {
      int sum = dp[k] + nums[j];
      if (nums[j] > nums[k] && sum > dp[j]) dp[j] = sum;
    }
    largest = std::max(largest, dp[j]);
  }

  return largest;
}
