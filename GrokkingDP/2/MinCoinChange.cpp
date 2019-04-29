#include <climits>
#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

struct Num {
  int val;
};

int MinCoinChange(std::vector<int>& denoms, int amount, Method m);
int Brute(std::vector<int>& denoms, int amount, size_t i);
int Memoize(std::vector<int>& denoms, int amount, size_t i,
            std::vector<std::vector<Num*>>& dp);
int BU(std::vector<int>& denoms, int amount, std::vector<std::vector<int>>& dp);

int main(void) {
  std::vector<int> denoms = {1, 2, 3};
  std::vector<int> coins = {1, 5, 10, 25};
  Method m = Method::MEM;
  std::cout << MinCoinChange(denoms, 5, m) << ":"
            << MinCoinChange(denoms, 11, m) << ":"
            << MinCoinChange(coins, 14938, m);
  return 0;
}

int MinCoinChange(std::vector<int>& denoms, int amount, Method m) {
  std::vector<std::vector<Num*>> dp;
  std::vector<std::vector<int>> bu;
  switch (m) {
    case Method::BRUTE:
      return Brute(denoms, amount, 0);
    case Method::MEM:
      dp = std::vector<std::vector<Num*>>(denoms.size(), std::vector<Num*>(amount + 1));
      return Memoize(denoms, amount, 0, dp);
    case Method::BU:
      bu = std::vector<std::vector<int>>(denoms.size(), std::vector<int>(amount + 1));
      return BU(denoms, amount, bu);
  }
};

int Brute(std::vector<int>& denoms, int amount, size_t i) {
  if (amount == 0) return 0;
  if (amount < 0 || i == denoms.size()) return INT_MAX;
  int count1 = INT_MAX;
  if (amount >= denoms[i]) {
    int res = Brute(denoms, amount - denoms[i], i);
    if (res != INT_MAX) count1 = res + 1;
  }
  return std::min(count1, Brute(denoms, amount, i + 1));
};

int Memoize(std::vector<int>& denoms, int amount, size_t i,
            std::vector<std::vector<Num*>>& dp) {
  if (amount == 0) return 0;
  if (amount < 0 || i == denoms.size()) return INT_MAX;
  if (dp[i][amount] == nullptr) {
    dp[i][amount] = new Num();
    int count1 = INT_MAX;
    if (amount >= denoms[i]) {
      int tmp = Memoize(denoms, amount - denoms[i], i, dp);
      if (tmp != INT_MAX)
        count1 = tmp + 1;
    }
    dp[i][amount]->val = std::min(count1, Memoize(denoms, amount, i + 1, dp));
  }
  return dp[i][amount]->val;
};

int BU(std::vector<int>& denoms, int amount, std::vector<std::vector<int>>& dp) {
  for (size_t i = 0; i < denoms.size(); ++i) {
    for (int s = 0; s <= amount; ++s) {
      if (i > 0) {
        dp[i][s] = std::min(dp[i - 1][s], 1 + dp[i][s - denoms[i]]);
      } else {
        dp[i][s] = s / denoms[i];
      }
    }
  }
  return dp[denoms.size() - 1][amount];
};
