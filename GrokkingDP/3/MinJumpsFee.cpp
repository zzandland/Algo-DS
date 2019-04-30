#include <climits>
#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int MinJumpFee(int n_stair, std::vector<int>& fees, Method m);
int Brute(int n_stair, std::vector<int>& fees);
int Memoize(int n_stair, std::vector<int>& fees, std::vector<int>& dp);
int BU(int n_stair, std::vector<int>& fees, std::vector<int>& dp);

int main(void) {
  std::vector<int> fee = {1, 2, 5, 2, 1, 2};
  std::vector<int> fee1 = {1, 2, 5, 2, 1, 2, 5, 2, 3, 5, 1, 2, 3, 6, 7, 2, 3};
  std::vector<int> fee2 = {2, 3, 4, 5};
  Method m = Method::BU;
  std::cout << MinJumpFee(fee.size(), fee, m) << ":"
            << MinJumpFee(fee1.size(), fee1, m) << ":"
            << MinJumpFee(4, fee2, m);
  return 0;
}

int MinJumpFee(int n_stair, std::vector<int>& fees, Method m) {
  std::vector<int> dp(n_stair + 1);
  switch (m) {
    case Method::BRUTE:
      return Brute(n_stair, fees);
    case Method::MEM:
      return Memoize(n_stair, fees, dp);
    case Method::BU:
      return BU(n_stair, fees, dp);
  }
}

int Brute(int n_stair, std::vector<int>& fees) {
  if (n_stair == 0) return 0;
  if (n_stair < 0) return INT_MAX;
  int fee = fees[fees.size() - n_stair];
  int min_fee = INT_MAX;
  for (int i = 3; i >= 1; --i) {
    int tmp = Brute(n_stair - i, fees);
    if (tmp != INT_MAX) min_fee = std::min(min_fee, tmp);
  }
  return min_fee == INT_MAX ? INT_MAX : min_fee + fee;
}

int Memoize(int n_stair, std::vector<int>& fees, std::vector<int>& dp) {
  if (n_stair == 0) return 0;
  if (n_stair < 0) return INT_MAX;
  if (dp[n_stair] == 0) {
    int fee = fees[fees.size() - n_stair];
    int min_fee = INT_MAX;
    for (int i = 3; i >= 1; --i) {
      int tmp = Memoize(n_stair - i, fees, dp);
      if (tmp != INT_MAX) min_fee = std::min(min_fee, tmp);
    }
    dp[n_stair] = min_fee == INT_MAX ? INT_MAX : min_fee + fee;
  }
  return dp[n_stair];
}

int BU(int n_stair, std::vector<int>& fees, std::vector<int>& dp) {
  dp[0] = 0;
  dp[1] = dp[2] = dp[3] = fees[0];
  for (int i = 3; i < n_stair; ++i)
    dp[i + 1] = std::min(dp[i] + fees[i], std::min(dp[i - 1] + fees[i - 1],
                                                   dp[i - 2] + fees[i - 2]));
  return dp[n_stair];
}
