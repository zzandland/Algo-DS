#include <iostream>
#include <vector>

enum class Method { BRUTE, MEMOIZE, BU };

int RodCutting(std::vector<int>& lengths, std::vector<int>& prices,
               int total_length, Method m);
int Brute(std::vector<int>& lengths, std::vector<int>& prices, int total_length,
          size_t i);
int Memoize(std::vector<int>& lengths, std::vector<int>& prices,
            int total_length, size_t i, std::vector<std::vector<int>>& dp);
int BU(std::vector<int>& lengths, std::vector<int>& prices, int total_length,
       std::vector<std::vector<int>>& dp);
int PrintSelected(std::vector<int>& lengths, std::vector<int>& prices, std::vector<std::vector<int>>& dp);

int main(void) {
  std::vector<int> lengths = {1, 2, 3, 4, 5};
  std::vector<int> prices = {2, 6, 7, 10, 13};
  Method m = Method::BU;
  std::cout << RodCutting(lengths, prices, 5, m);
  return 0;
}

int RodCutting(std::vector<int>& lengths, std::vector<int>& prices,
               int total_length, Method m) {
  std::vector<std::vector<int>> dp(lengths.size(), std::vector<int>(total_length + 1));
  switch (m) {
    case Method::BRUTE:
      return Brute(lengths, prices, total_length, 0);
    case Method::MEMOIZE:
      return Memoize(lengths, prices, total_length, 0, dp);
    case Method::BU:
      return BU(lengths, prices, total_length, dp);
  }
  return 0;
}

int Brute(std::vector<int>& lengths, std::vector<int>& prices, int total_length,
          size_t i) {
  if (total_length <= 0 || i == lengths.size()) return 0;
  int price1 = 0;
  if (total_length >= lengths[i])
    price1 = prices[i] + Brute(lengths, prices, total_length - lengths[i], i);
  int price2 = Brute(lengths, prices, total_length, i + 1);
  return std::max(price1, price2);
};

int Memoize(std::vector<int>& lengths, std::vector<int>& prices,
            int total_length, size_t i, std::vector<std::vector<int>>& dp) {
  if (total_length <= 0 || i == lengths.size()) return 0;
  if (dp[i][total_length] != 0) return dp[i][total_length];
  int price1 = 0;
  if (total_length >= lengths[i]) {
    price1 =
        prices[i] + Memoize(lengths, prices, total_length - lengths[i], i, dp);
  }
  int price2 = Memoize(lengths, prices, total_length, i + 1, dp);
  dp[i][total_length] = std::max(price1, price2);
  return dp[i][total_length];
};

int BU(std::vector<int>& lengths, std::vector<int>& prices, int total_length,
       std::vector<std::vector<int>>& dp) {
  for (size_t i = 0; i < lengths.size(); ++i)
    dp[i][0] = 0;
  for (int s = 1; s <= total_length; ++s)
    dp[0][s] = prices[0] * (s / lengths[0]);
  for (size_t i = 1; i < lengths.size(); ++i) {
    for (int s = 1; s <= total_length; ++s) {
      int new_price = prices[i] * (s / lengths[i]) + dp[i - 1][s % lengths[i]];
      dp[i][s] = std::max(dp[i - 1][s], new_price);
    }
  }
  PrintSelected(lengths, prices, dp);
  return dp[lengths.size() - 1][total_length];
};

int PrintSelected(std::vector<int>& lengths, std::vector<int>& prices, std::vector<std::vector<int>>& dp) {
  int i = dp.size() - 1;
  int s = dp[0].size() - 1;
  std::cout << "Selected lengths are: ";
  while (i > 0 && s > 0) {
    if (dp[i][s] == dp[i - 1][s])
      i -= 1;
    else {
      std::cout << lengths[i] << " ";
      s -= lengths[i];
    }
  }
  while (s > 0) {
    std::cout << lengths[0] << " ";
    s -= lengths[0];
  }
};
