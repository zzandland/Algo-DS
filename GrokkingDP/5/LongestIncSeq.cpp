#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

struct Int {
  int val;
};

int LongestIncreasingSeq(std::vector<int>& nums, Method m);
int Brute(std::vector<int>& nums, int i, int j);
int Memoize(std::vector<int>& nums, int i, int j,
            std::vector<std::vector<Int*>>& dp);
int BU(std::vector<int>& nums);

int main(void) {
  std::vector<int> s1 = {4, 2, 3, 6, 10, 1, 12};
  std::vector<int> s2 = {-4, 10, 3, 7, 15};
  Method m = Method::BU;
  std::cout << LongestIncreasingSeq(s1, m) << ":"
            << LongestIncreasingSeq(s2, m);
  return 0;
}

int LongestIncreasingSeq(std::vector<int>& nums, Method m) {
  std::vector<std::vector<Int*>> dp(nums.size() + 1,
                                    std::vector<Int*>(nums.size() + 1));
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
  int count = 0;
  if (j == -1 || nums[i] > nums[j]) count = 1 + Brute(nums, i + 1, i);
  return std::max(Brute(nums, i + 1, j), count);
}

int Memoize(std::vector<int>& nums, int i, int j,
            std::vector<std::vector<Int*>>& dp) {
  if (i == (int)nums.size()) return 0;
  if (dp[i][j + 1] == nullptr) {
    dp[i][j + 1] = new Int();
    int count = 0;
    if (j == -1 || nums[i] > nums[j]) count = 1 + Memoize(nums, i + 1, i, dp);
    dp[i][j + 1]->val = std::max(Memoize(nums, i + 1, j, dp), count);
  }
  return dp[i][j + 1]->val;
}

int BU(std::vector<int>& nums) {
  std::vector<int> dp(nums.size(), 1);
  int longest = 1;
  for (size_t i = 1; i < nums.size(); ++i) {
    for (size_t j = 0; j < i; ++j) {
      if (nums[i] > nums[j] && dp[i] <= dp[j]) {
        dp[i] = dp[j] + 1;
        longest = std::max(longest, dp[i]);
      }
    }
  }
  return longest;
}
