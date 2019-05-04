#include <iostream>
#include <vector>

enum class Method { BRUTE, BU };

int MinDeltoSortedSeq(std::vector<int>& nums, Method m);
int Brute(std::vector<int>& nums, int i, int j);
int BU(std::vector<int>& nums);

int main(void) {
  std::vector<int> s1 = {4, 2, 3, 6, 10, 1, 12};
  std::vector<int> s2 = {-4, 10, 3, 7, 15};
  std::vector<int> s3 = {3, 2, 1, 0};
  Method m = Method::BU;
  std::cout << MinDeltoSortedSeq(s1, m) << ":" << MinDeltoSortedSeq(s2, m)
            << ":" << MinDeltoSortedSeq(s3, m);
  return 0;
}

int MinDeltoSortedSeq(std::vector<int>& nums, Method m) {
  switch (m) {
    case Method::BRUTE:
      return nums.size() - Brute(nums, 0, -1);
    case Method::BU:
      return nums.size() - BU(nums);
  }
}

int Brute(std::vector<int>& nums, int i, int j) {
  if (i == (int)nums.size()) return 0;
  int with = 0;
  if (j == -1 || nums[i] > nums[j]) with = 1 + Brute(nums, i + 1, i);
  return std::max(with, Brute(nums, i + 1, j));
}

int BU(std::vector<int>& nums) {
  int n = nums.size();
  std::vector<int> dp(n, 1);
  int longest = 1;
  for (int i = 1; i < n; ++i) {
    for (int j = 0; j < i; ++j)
      if (nums[i] > nums[j] && dp[j] >= dp[i]) {
        dp[i] = dp[j] + 1;
        longest = std::max(longest, dp[n - 1]);
      }
  }
  return longest;
}
