#include <iostream>
#include <vector>

enum class Method { BRUTE_FORCE, MEMOIZE, BOTTOM_UP };

struct Num {
  int val;
};

int TargetSum(std::vector<int>& nums, int sum, Method m);
int BruteForce(std::vector<int>& nums, int sum, size_t i);
int Memoize(std::vector<int>& nums, int sum, size_t i, int target, int total,
            std::vector<std::vector<Num*>>& dp);

int main(void) {
  std::vector<int> ex1 = {1, 1, 2, 3};
  std::vector<int> ex2 = {1, 2, 7, 1};
  Method m = Method::MEMOIZE;
  std::cout << TargetSum(ex1, 1, m);
  // std::cout << TargetSum(ex1, 1, m) << ":" << TargetSum(ex2, 9, m);
  return 0;
}

int TargetSum(std::vector<int>& nums, int sum, Method m) {
  int total = 0;
  for (int n : nums) total += n;
  std::vector<std::vector<Num*>> dp;
  switch (m) {
    case Method::BRUTE_FORCE:
      return BruteForce(nums, sum, 0);
    case Method::MEMOIZE:
      dp = std::vector<std::vector<Num*>>(nums.size(),
                                          std::vector<Num*>(total * 2 + 1));
      return Memoize(nums, 0, 0, sum, total, dp);
  }
};

int BruteForce(std::vector<int>& nums, int sum, size_t i) {
  if (nums.size() == 0) return 0;
  if (i == nums.size()) return sum == 0 ? 1 : 0;
  return BruteForce(nums, sum - nums[i], i + 1) +
         BruteForce(nums, sum + nums[i], i + 1);
};

int Memoize(std::vector<int>& nums, int sum, size_t i, int target, int total,
            std::vector<std::vector<Num*>>& dp) {
  if (i == nums.size()) return sum == target ? 1 : 0;
  int index = sum + total;
  if (dp[i][index] == nullptr) {
    dp[i][index] = new Num;
    int val = Memoize(nums, sum + nums[i], i + 1, target, total, dp) +
              Memoize(nums, sum - nums[i], i + 1, target, total, dp);
    dp[i][index]->val = val;
  }
  return dp[i][index]->val;
};
