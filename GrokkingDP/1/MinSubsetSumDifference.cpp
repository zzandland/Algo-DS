#include <cmath>
#include <iostream>
#include <vector>

enum class Method { BRUTE_FORCE, MEMOIZE, BOTTOM_UP };

int MinSubSumDifference(std::vector<int>& nums, Method m);

int BruteForce(std::vector<int>& nums, size_t i, int set1, int set2);

int Memoize(std::vector<int>& nums, size_t i, int set1, int set2,
            std::vector<std::vector<int*>>& dp);

int BU(std::vector<int>& nums, int sum, std::vector<bool>& dp);

int main(void) {
  std::vector<int> ex1 = {1, 2, 3, 9};
  std::vector<int> ex2 = {1, 2, 7, 1, 5};
  std::vector<int> ex3 = {1, 3, 100, 4};
  Method m = Method::BOTTOM_UP;
  std::cout << MinSubSumDifference(ex1, m) << std::endl
            << MinSubSumDifference(ex2, m) << std::endl
            << MinSubSumDifference(ex3, m);
  return 0;
}

int MinSubSumDifference(std::vector<int>& nums, Method m) {
  int sum = 0;
  for (int n : nums) sum += n;
  std::vector<std::vector<int*>> dp;
  switch (m) {
    case Method::BRUTE_FORCE:
      return BruteForce(nums, 0, 0, 0);
    case Method::MEMOIZE:
      dp = std::vector<std::vector<int*>>(nums.size(), std::vector<int*>(sum));
      return Memoize(nums, 0, 0, 0, dp);
    case Method::BOTTOM_UP:
      std::vector<bool> bu(sum / 2 + 1);
      return BU(nums, sum, bu);
  }
};

int BruteForce(std::vector<int>& nums, size_t i, int set1, int set2) {
  if (i == nums.size()) return std::abs(set1 - set2);
  return std::min(BruteForce(nums, i + 1, set1 + nums[i], set2),
                  BruteForce(nums, i + 1, set1, set2 + nums[i]));
};

int Memoize(std::vector<int>& nums, size_t i, int set1, int set2,
            std::vector<std::vector<int*>>& dp) {
  if (i == nums.size()) return std::abs(set1 - set2);
  if (dp[i][set1] != nullptr) return *dp[i][set1];
  int min_diff = std::min(Memoize(nums, i + 1, set1 + nums[i], set2, dp),
                          Memoize(nums, i + 1, set1, set2 + nums[i], dp));
  dp[i][set1] = &min_diff;
  return *dp[i][set1];
};

int BU(std::vector<int>& nums, int sum, std::vector<bool>& dp) {
  dp[0] = true;
  for (size_t s = 1; s < dp.size(); ++s)
    if (nums[0] >= (int)s) dp[s] = true;
  for (size_t i = 1; i < nums.size(); ++i) {
    for (size_t s = dp.size() - 1; s >= 1; --s)
      if (nums[i] <= (int)s) dp[s] = dp[s - nums[i]];
  }
  for (size_t s = dp.size() - 1; s >= 0; --s) {
    if (dp[s]) return sum - (2 * (int)s);
  }
};
