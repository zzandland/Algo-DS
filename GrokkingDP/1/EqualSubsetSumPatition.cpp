#include <iostream>
#include <vector>

enum class Method { BRUTE_FORCE, MEMOIZATION, BOTTOM_UP };

bool CanPartition(std::vector<int>& nums, Method m);
bool CanPartition(std::vector<int>& nums, size_t i, int sum);
bool CanPartitionMem(std::vector<int>& nums, size_t i, int sum,
                     std::vector<std::vector<bool>>& dp);
bool CanPartitionBU(std::vector<int>& nums, int sum, std::vector<bool>& dp);

int main(void) {
  std::vector<int> n1 = {1, 2, 3, 4};
  std::vector<int> n2 = {3, 4, 1, 7, 1};
  std::vector<int> n3 = {3, 6, 4, 2};
  std::vector<int> n4;
  for (int i = 0; i < 20001; ++i) {
    int val = std::rand() % 100 + 1;
    n4.push_back(val);
  }
  Method m = Method::MEMOIZATION;
  std::cout << CanPartition(n1, m) << ":" << CanPartition(n2, m) << ":"
            << CanPartition(n3, m) << ":" << CanPartition(n4, m);
  return 0;
}

bool CanPartition(std::vector<int>& nums, Method m) {
  int sum = 0;
  for (int n : nums) sum += n;
  if (sum % 2 == 1) return false;
  std::vector<std::vector<bool>> dp;
  switch (m) {
    case Method::BRUTE_FORCE:
      return CanPartition(nums, 0, sum / 2);
    case Method::MEMOIZATION:
      dp = std::vector<std::vector<bool>>(nums.size(),
                                          std::vector<bool>(sum / 2 + 1));
      return CanPartitionMem(nums, 0, sum / 2, dp);
    case Method::BOTTOM_UP:
      std::vector<bool> bu(sum / 2 + 1);
      return CanPartitionBU(nums, sum / 2, bu);
  }
  return false;
};

bool CanPartition(std::vector<int>& nums, size_t i, int sum) {
  if (sum == 0) return true;
  if (sum < 0 || i == nums.size()) return false;
  bool with = false;
  if (sum >= nums[i]) with = CanPartition(nums, i + 1, sum - nums[i]);
  return with || CanPartition(nums, i + 1, sum);
};

bool CanPartitionMem(std::vector<int>& nums, size_t i, int sum,
                     std::vector<std::vector<bool>>& dp) {
  if (i == nums.size()) return false;
  if (sum == 0 || dp[i][sum]) return true;
  if (sum >= nums[i]) {
    if (CanPartitionMem(nums, i + 1, sum - nums[i], dp)) {
      dp[i][sum] = true;
      return true;
    }
  }
  dp[i][sum] = CanPartitionMem(nums, i + 1, sum, dp);
  return dp[i][sum];
};

bool CanPartitionBU(std::vector<int>& nums, int sum, std::vector<bool>& dp) {
  dp[0] = true;
  for (int s = 1; s < sum; ++s)
    if (nums[0] <= s) dp[s] = true;
  for (size_t i = 1; i < nums.size(); ++i) {
    for (size_t s = sum; s >= 1; --s) {
      if (nums[i] <= (int)s) dp[s] = dp[s - nums[i]];
    }
    if (dp[sum]) return true;
  }
  return dp[sum];
};
