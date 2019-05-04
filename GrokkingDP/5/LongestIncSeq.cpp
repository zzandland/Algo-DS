#include <iostream>
#include <vector>

enum class Method {
  BRUTE, MEM, BU
};

struct Int {
 int val;
};

int LongestIncreasingSequence(std::vector<int>& seq, Method m);
int Brute(std::vector<int>& seq, int curr_i, int prev_i);
int Memoize(std::vector<int>& seq, int curr_i, int prev_i, std::vector<std::vector<Int*>>& dp);
int BU(std::vector<int>& seq);

int main(void)
{
  std::vector<int> s1 = {4, 2, 3, 6, 10, 1, 2, 12};
  std::vector<int> s2 = {-4, 10, 3, 7, 15};
  std::vector<int> s3 = {-4,10,3,7,15,2,10,-2,-5,25,-1,-15,25,23,56,6,1,2,5,1,2,6,1,-2};
  Method m = Method::BU;
  std::cout << LongestIncreasingSequence(s1, m) << ":"
            << LongestIncreasingSequence(s2, m) << ":"
            << LongestIncreasingSequence(s3, m);
  return 0;
}

int LongestIncreasingSequence(std::vector<int>& seq, Method m) {
  std::vector<std::vector<Int*>> dp(seq.size() + 1, std::vector<Int*>(seq.size() + 1));
  switch (m) {
    case Method::BRUTE:
      return Brute(seq, 0, -1);
    case Method::MEM:
      return Memoize(seq, 0, -1, dp);
    case Method::BU:
      return BU(seq);
  }
}

int Brute(std::vector<int>& seq, int curr_i, int prev_i) {
  if (curr_i == (int)seq.size()) return 0;
  int c1 = 0;
  if (prev_i == -1 || seq[curr_i] > seq[prev_i])
    c1 = 1 + Brute(seq, curr_i + 1, curr_i);
  int c2 = Brute(seq, curr_i + 1, prev_i);
  return std::max(c1, c2);
}

int Memoize(std::vector<int>& seq, int curr_i, int prev_i, std::vector<std::vector<Int*>>& dp) {
  if (curr_i == (int)seq.size()) return 0;
  if (dp[curr_i][prev_i + 1] == nullptr) {
    dp[curr_i][prev_i + 1] = new Int();
    int c1 = 0;
    if (prev_i == -1 || seq[curr_i] > seq[prev_i])
      c1 = 1 + Memoize(seq, curr_i + 1, curr_i, dp);
    int c2 = Memoize(seq, curr_i + 1, prev_i, dp);
    dp[curr_i][prev_i + 1]->val = std::max(c1, c2);
  }
  return dp[curr_i][prev_i + 1]->val;
}

int BU(std::vector<int>& seq) {
}
