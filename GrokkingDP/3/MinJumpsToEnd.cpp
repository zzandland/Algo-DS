#include <iostream>
#include <climits>
#include <vector>

enum class Method {
  BRUTE, MEM, BU
};

int MinJumpsToEnd(std::vector<int>& nums, Method m);
int Brute(std::vector<int>& nums, size_t i);
int Memoize(std::vector<int>& nums, size_t i, std::vector<int>& dp);
int BU(std::vector<int>& nums);

int main(void)
{
  std::vector<int> n1 = {2, 1, 1, 1, 4};  
  std::vector<int> n2 = {1,1,3,6,9,3,0,1,3,5,2,1,2,3,2,6,2,4,3,2,1,2,1,2,1,1,2,3,4,5,2,1,2,7,8,5,7,5,12,2,6,3,2};
  Method m = Method::BU;
  std::cout << MinJumpsToEnd(n1, m) << ":" << MinJumpsToEnd(n2, m);
  return 0;
}

int MinJumpsToEnd(std::vector<int>& nums, Method m) {
  std::vector<int> dp(nums.size() + 1);
  switch (m) {
    case Method::BRUTE:
      return Brute(nums, 0);
    case Method::MEM:
      return Memoize(nums, 0, dp);
    case Method::BU:
      return BU(nums);
  }  
}

int Brute(std::vector<int>& nums, size_t i) {
  if (i == nums.size() - 1) return 0;
  if (nums[i] == 0) return INT_MAX;
  int inc = INT_MAX;
  for (size_t j = nums[i]; j >= 1; --j) {
    int res = INT_MAX;
    if (i + j <= nums.size() - 1) {
      int tmp = Brute(nums, i + j);
      if (tmp != INT_MAX) res = 1 + tmp;
    }
    inc = std::min(inc, res);
  }
  return inc;
}

int Memoize(std::vector<int>& nums, size_t i, std::vector<int>& dp) {
  if (i == nums.size() - 1) return 0;
  if (nums[i] == 0) return INT_MAX;
  if (dp[i] == 0) {
    int inc = INT_MAX;
    for (size_t j = nums[i]; j >= 1; --j) {
      int res = INT_MAX;
      if (i + j <= nums.size() - 1) {
        int tmp = Memoize(nums, i + j, dp);
        if (tmp != INT_MAX) res = 1 + tmp;
      }
      inc = std::min(inc, res);
    }
    dp[i] = inc;
  }
  return dp[i];
}

int BU(std::vector<int>& nums) {
  std::vector<int> dp(nums.size() + 1);
  for (size_t i = 1; i < nums.size(); ++i)
    dp[i] = INT_MAX;
  for (size_t i = 0; i < nums.size() - 1; ++i) {
    for (size_t j = i + 1; j <= i + nums[i] && j < nums.size(); ++j) {
      dp[j] = std::min(dp[j], dp[i] + 1);
    }
  }
  return dp[nums.size() - 1];
}
