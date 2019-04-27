#include <iostream>
#include <vector>

enum class Method { BRUTE_FORCE, MEMOIZE, BOTTOM_UP };

struct Num {
  int val;
};

int TargetSum(std::vector<int>& nums, int sum, Method m);
// int BruteForce(std::vector<int>& nums, int sum, size_t i);
// int Memoize(std::vector<int>& nums, int sum, size_t i, int target, int total,
// std::vector<std::vector<Num*>>& dp);
int CountSubSum(std::vector<int>& nums, int sum, std::vector<int>& dp);

int main(void) {
  std::vector<int> ex1 = {1, 1, 2, 3};
  std::vector<int> ex2 = {1, 2, 7, 1};
  Method m = Method::BOTTOM_UP;
  std::cout << TargetSum(ex1, 1, m) << ":" << TargetSum(ex2, 9, m);
  return 0;
}

int TargetSum(std::vector<int>& nums, int sum, Method m) {
  int total = 0;
  for (int n : nums) total += n;
  // std::vector<std::vector<Num*>> dp;
  std::vector<int> dp;
  int offset = (sum + total) / 2;
  switch (m) {
    case Method::BRUTE_FORCE:
      // return BruteForce(nums, sum, 0);
      return 0;
    case Method::MEMOIZE:
      // dp = std::vector<std::vector<Num*>>(nums.size(),
      // std::vector<Num*>(total * 2 + 1));
      // return Memoize(nums, 0, 0, sum, total, dp);
      return 0;
    case Method::BOTTOM_UP:
      dp = std::vector<int>(offset + 1);
      return CountSubSum(nums, offset, dp);
  }
  return 0;
};

int CountSubSum(std::vector<int>& nums, int sum, std::vector<int>& dp) {
  dp[0] = 1;
  for (int s = 0; s <= sum; ++s)
    if (s <= nums[0]) dp[s] = 1;
  for (size_t i = 1; i < nums.size(); ++i) {
    for (int s = sum; s >= 1; --s)
      if (s >= nums[i]) dp[s] += dp[s - nums[i]];
  }
  return dp[sum];
}

// int BruteForce(std::vector<int>& nums, int sum, size_t i) {
// if (nums.size() == 0) return 0;
// if (i == nums.size()) return sum == 0 ? 1 : 0;
// return BruteForce(nums, sum - nums[i], i + 1) +
// BruteForce(nums, sum + nums[i], i + 1);
// };

// int Memoize(std::vector<int>& nums, int sum, size_t i, int target, int total,
// std::vector<std::vector<Num*>>& dp) {
// if (i == nums.size()) return sum == target ? 1 : 0;
// int index = sum + total;
// if (dp[i][index] == nullptr) {
// dp[i][index] = new Num;
// int val = Memoize(nums, sum + nums[i], i + 1, target, total, dp) +
// Memoize(nums, sum - nums[i], i + 1, target, total, dp);
// dp[i][index]->val = val;
// }
// return dp[i][index]->val;
// };
