#include <iostream>
#include <vector>

enum class Method { BRUTE_FORCE, MEMOIZE, BOTTOM_UP };

int CountSubSum(std::vector<int>& nums, int target, Method m);
int BruteForce(std::vector<int>& nums, int sum, size_t i);
int Memoize(std::vector<int>& nums, int sum, size_t i,
            std::vector<std::vector<int>>& dp);
int BU(std::vector<int>& nums, int target, std::vector<int>& dp);

int main(void) {
  std::vector<int> ex1 = {1, 1, 2, 3};
  std::vector<int> ex2 = {1, 2, 7, 1, 5};
  Method m = Method::MEMOIZE;
  std::cout << CountSubSum(ex1, 4, m) << ":" << CountSubSum(ex2, 9, m);
  return 0;
}

int CountSubSum(std::vector<int>& nums, int target, Method m) {
  int sum = 0;
  for (int n : nums) sum += n;
  std::vector<std::vector<int>> dp;
  switch (m) {
    case Method::BRUTE_FORCE:
      return BruteForce(nums, target, 0);
    case Method::MEMOIZE:
      dp =
          std::vector<std::vector<int>>(nums.size(), std::vector<int>(sum + 1));
      return Memoize(nums, target, 0, dp);
    case Method::BOTTOM_UP:
      std::vector<int> bu(target + 1);
      return BU(nums, target, bu);
  }
};

int BruteForce(std::vector<int>& nums, int sum, size_t i) {
  if (sum == 0) return 1;
  if (nums.size() == 0 || i == nums.size()) return 0;
  int output = 0;
  if (sum - nums[i] >= 0) output = BruteForce(nums, sum - nums[i], i + 1);
  return output + BruteForce(nums, sum, i + 1);
};

int Memoize(std::vector<int>& nums, int sum, size_t i,
            std::vector<std::vector<int>>& dp) {
  if (sum == 0) return 1;
  if (nums.size() == 0 || i == nums.size()) return 0;
  if (dp[i][sum] != 0) return dp[i][sum];
  int output = 0;
  if (sum - nums[i] >= 0)
    output = Memoize(nums, sum - nums[i], i + 1, dp);
  dp[i][sum] = output + Memoize(nums, sum, i + 1, dp);
  return dp[i][sum];
};

int BU(std::vector<int>& nums, int target, std::vector<int>& dp) {
  dp[0] = 1;
  for (int s = 1; s <= target; ++s)
    if (nums[0] >= s) dp[s] = 1;
  for (size_t i = 1; i < nums.size(); ++i) {
    for (int s = target; s >= 1; --s) {
      if (nums[i] <= s) dp[s] += dp[s - nums[i]];
    }
  }
  return dp[target];
};
