#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int LongestBitonicSubseq(std::vector<int>& nums, Method m);
int Brute(std::vector<int>& nums);
int LeftHalf(std::vector<int>& nums, size_t i, int j, size_t pivot);
int RightHalf(std::vector<int>& nums, size_t i, int j, size_t pivot);
int Memoize(std::vector<int>& nums);
int LeftHalfMem(std::vector<int>& nums, size_t i, int j, size_t pivot, std::vector<std::vector<int>>& dp);
int RightHalfMem(std::vector<int>& nums, size_t i, int j, size_t pivot, std::vector<std::vector<int>>& dp);
int BU(std::vector<int>& nums);

int main(void)
{
  std::vector<int> n1 = {4,2,3,6,10,1,12};
  std::vector<int> n2 = {4,2,5,9,7,6,10,3,1};
  std::vector<int> n3 = {6,5,4,3,2,1};
  Method m = Method::BU;
  std::cout << LongestBitonicSubseq(n1, m) << ":"
            << LongestBitonicSubseq(n2, m) << ":"
            << LongestBitonicSubseq(n3, m);
  return 0;
}

int LongestBitonicSubseq(std::vector<int>& nums, Method m) {
  switch (m) {
    case Method::BRUTE:
      return Brute(nums);
    case Method::MEM:
      return Memoize(nums);
    case Method::BU:
      return BU(nums);
  }
}

int Brute(std::vector<int>& nums) {
  int longest = 0;
  for (size_t i = 0; i < nums.size(); ++i) {
    int len = LeftHalf(nums, 0, -1, i) + RightHalf(nums, i, i - 1, i) - 1;
    longest = std::max(longest, len);
  }
  return longest;
}

int LeftHalf(std::vector<int>& nums, size_t i, int j, size_t pivot) {
  std::cout << "enter ";
  if (i > pivot) return 0;
  int include = 0;
  if (j == -1 || nums[i] > nums[j])
    include = 1 + LeftHalf(nums, i + 1, i, pivot);
  return std::max(include, LeftHalf(nums, i + 1, j, pivot));
}

int RightHalf(std::vector<int>& nums, size_t i, int j, size_t pivot) {
  if (i == nums.size()) return 0;
  int include = 0;
  if (j < (int)pivot || nums[i] < nums[j])
    include = 1 + RightHalf(nums, i + 1, i, pivot);
  return std::max(include, RightHalf(nums, i + 1, j, pivot));
}

int Memoize(std::vector<int>& nums) {
  int n = nums.size();
  int longest = 0;
  for (int i = 0; i < n; ++i) {
    std::vector<std::vector<int>> inc_dp(n, std::vector<int>(n));
    std::vector<std::vector<int>> dec_dp(n, std::vector<int>(n));
    int len = LeftHalfMem(nums, 0, -1, i, inc_dp) + RightHalfMem(nums, i, i - 1, i, dec_dp) - 1;
    longest = std::max(longest, len);
  }
  return longest;
}

int LeftHalfMem(std::vector<int>& nums, size_t i, int j, size_t pivot, std::vector<std::vector<int>>& dp) {
  if (i > pivot) return 0;
  if (dp[i][j + 1] == 0) {
    int include = 0;
    if (nums[i] > nums[j] || j == -1)
      include = 1 + LeftHalfMem(nums, i + 1, i, pivot, dp);
    dp[i][j + 1] = std::max(include, LeftHalfMem(nums, i + 1, j, pivot, dp));
  }
  return dp[i][j + 1];
}

int RightHalfMem(std::vector<int>& nums, size_t i, int j, size_t pivot, std::vector<std::vector<int>>& dp) {
  if (i == nums.size()) return 0;
  if (dp[i][j + 1] == 0) {
    int include = 0;
    if (nums[i] < nums[j] || j < (int)pivot)
      include = 1 + RightHalfMem(nums, i + 1, i, pivot, dp);
    dp[i][j + 1] = std::max(include, RightHalfMem(nums, i + 1, j, pivot, dp));
  }
  return dp[i][j + 1];
}

int BU(std::vector<int>& nums) {
  int n = nums.size();
  std::vector<int> left_half(n, 1);
  for (int i = 1; i < n; ++i) {
    for (int j = i - 1; j >= 0; --j)
      if (nums[i] > nums[j])
        left_half[i] = std::max(left_half[i], left_half[j] + 1);
  }

  std::vector<int> right_half(n, 1);
  for (int i = n - 1; i >= 0; --i) {
    for (int j = i + 1; j < n; ++j)
      if (nums[i] > nums[j])
        right_half[i] = std::max(right_half[i], right_half[j] + 1);
  }

  int longest = 0;
  for (size_t i = 0; i < nums.size(); ++i) {
    int len = left_half[i] + right_half[i] - 1;
    longest = std::max(longest, len);
  }
  return longest;
}
