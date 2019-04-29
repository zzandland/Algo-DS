#include <chrono>
#include <iostream>
#include <vector>

typedef std::chrono::high_resolution_clock Clock;

enum class Method { BRUTE, MEM, BU };

int CoinChange(std::vector<int>& denoms, int amount, Method m);
int Brute(std::vector<int>& denoms, int amount, size_t i);
int Memoize(std::vector<int>& denoms, int amount, size_t i,
            std::vector<std::vector<int>>& dp);
int BU(std::vector<int>& denoms, int amount, std::vector<std::vector<int>>& dp);

int main(void) {
  std::vector<int> denoms = {1, 5, 10, 25, 50};
  Method m = Method::BU;
  auto t1 = Clock::now();
  std::cout << CoinChange(denoms, 938201, m);
  auto t2 = Clock::now();
  std::cout
      << "\nOperation took: "
      << std::chrono::duration_cast<std::chrono::nanoseconds>(t2 - t1).count() /
             1000000
      << " ms.";
  return 0;
}

int CoinChange(std::vector<int>& denoms, int amount, Method m) {
  std::vector<std::vector<int>> dp(denoms.size(), std::vector<int>(amount + 1));
  switch (m) {
    case Method::BRUTE:
      return Brute(denoms, amount, 0);
    case Method::MEM:
      return Memoize(denoms, amount, 0, dp);
    case Method::BU:
      return BU(denoms, amount, dp);
  }
};

int Brute(std::vector<int>& denoms, int amount, size_t i) {
  if (amount == 0) return 1;
  if (amount < 0 || i == denoms.size()) return 0;
  int inc = 0;
  if (amount >= denoms[i]) inc = Brute(denoms, amount - denoms[i], i);
  return inc + Brute(denoms, amount, i + 1);
};

int Memoize(std::vector<int>& denoms, int amount, size_t i,
            std::vector<std::vector<int>>& dp) {
  if (amount == 0) return 1;
  if (amount < 0 || i == denoms.size()) return 0;
  if (dp[i][amount] != 0) return dp[i][amount];
  int inc = 0;
  if (amount >= denoms[i]) inc = Memoize(denoms, amount - denoms[i], i, dp);
  dp[i][amount] = inc + Memoize(denoms, amount, i + 1, dp);
  return dp[i][amount];
};

int BU(std::vector<int>& denoms, int amount,
       std::vector<std::vector<int>>& dp) {
  for (size_t i = 0; i < denoms.size(); ++i) dp[i][0] = 1;
  for (size_t i = 0; i < denoms.size(); ++i) {
    for (int s = 1; s <= amount; ++s) {
      if (i > 0) dp[i][s] = dp[i - 1][s];
      if (s >= denoms[i]) dp[i][s] += dp[i][s - denoms[i]];
    }
  }
  return dp[denoms.size() - 1][amount];
};
