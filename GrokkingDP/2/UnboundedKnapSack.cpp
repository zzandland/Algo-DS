#include <iostream>
#include <vector>

enum class Method { BRUTE, MEMOIZE, BU };

struct Item {
  int val;
  int weight;
};

int Wrapper(std::vector<Item*>& items, int capacity, Method m);

int Brute(std::vector<int>& weights, std::vector<int>& profits, int capacity,
          size_t i);
int Memoize(std::vector<int>& weights, std::vector<int>& profits,
            int capacity, size_t i, std::vector<std::vector<int>>& dp);
int BU(std::vector<int>& weights, std::vector<int>& profits, int capacity, std::vector<int>& bu);

int main(void) {
  Item apple = {15, 1};
  Item orange = {50, 3};
  Item melon = {60, 4};
  Item melon2 = {90, 5};
  std::vector<Item*> items = {&apple, &orange, &melon, &melon2};
  Method m = Method::BU;
  std::cout << Wrapper(items, 8, m) << ":" << Wrapper(items, 6, m);
  return 0;
}

int Wrapper(std::vector<Item*>& items, int capacity, Method m) {
  std::vector<int> weights;
  std::vector<int> profits;
  int total_weight = 0;
  for (Item* i : items) {
    weights.push_back(i->weight);
    profits.push_back(i->val);
    total_weight += i->weight;
  }
  std::vector<std::vector<int>> dp;
  switch (m) {
    case Method::BRUTE:
      return Brute(weights, profits, capacity, 0);
    case Method::MEMOIZE:
      dp = std::vector<std::vector<int>>(items.size(), std::vector<int>(total_weight + 1));
      return Memoize(weights, profits, capacity, 0, dp);
    case Method::BU:
      std::vector<int> bu(capacity + 1);
      return BU(weights, profits, capacity, bu);
  }
  return 0;
};

int Brute(std::vector<int>& weights, std::vector<int>& profits, int capacity,
          size_t i) {
  if (i == weights.size() || capacity <= 0) return 0;
  int profit1 = 0;
  if (capacity >= weights[i]) 
    profit1 = profits[i] + Brute(weights, profits, capacity - weights[i], i);
  int profit2 = Brute(weights, profits, capacity, i + 1);
  return std::max(profit1, profit2);
};

int Memoize(std::vector<int>& weights, std::vector<int>& profits,
            int capacity, size_t i, std::vector<std::vector<int>>& dp) {
  if (i == weights.size() || capacity <= 0) return 0;
  if (dp[i][capacity] != 0) return dp[i][capacity];
  int profit1 = 0;
  if (capacity >= weights[i]) 
    profit1 = profits[i] + Memoize(weights, profits, capacity - weights[i], i, dp);
  int profit2 = Memoize(weights, profits, capacity, i + 1, dp);
  dp[i][capacity] = std::max(profit1, profit2);
  return dp[i][capacity];
};

int BU(std::vector<int>& weights, std::vector<int>& profits, int capacity, std::vector<int>& bu) {
  bu[0] = 0;
  for (int s = 1; s <= capacity; ++s)
    bu[s] = profits[0] * (s / weights[0]);
  for (size_t i = 1; i < weights.size(); ++i) {
    for (int s = capacity; s >= 1; --s) {
      if (s >= weights[i]) bu[s] = std::max(bu[s], profits[i] + bu[s - weights[i]]);
    }
  }
  return bu[capacity];
};
