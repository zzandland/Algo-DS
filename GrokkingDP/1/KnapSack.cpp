#include <iostream>
#include <list>
#include <set>
#include <vector>

enum class Method { BRUTE_FORCE, MEMOIZE, BOTTOM_UP };

struct Item {
  char name;
  int value;
  int weight;
};

std::set<Item*> GetItemsMaxProfit(std::set<Item*>& items, int capacity);
std::list<Item*> GetItemsMaxProfit(std::list<Item*>& items,
                                   std::list<Item*>& selected, int capacity);

int GetMaxProfit(std::set<Item*>& items, int capacity, Method m);
int GetMaxProfit(std::vector<int>& profits, std::vector<int>& weights,
                 int capacity, size_t curr_index);
int GetMaxProfitMemoize(std::vector<int>& profits, std::vector<int>& weights,
                        int capacity, size_t curr_index,
                        std::vector<std::vector<int>>& dp);
int GetMaxProfitBottomUp(std::vector<int>& profits, std::vector<int>& weights,
                         std::vector<std::vector<int>>& dp);
int TotalWeight(const std::list<Item*>& items);
int TotalProfit(const std::list<Item*>& items);

int main(void) {
  Item a = {'A', 1, 1};
  Item b = {'B', 6, 2};
  Item c = {'C', 10, 3};
  Item d = {'D', 16, 5};
  std::set<Item*> items;
  items.insert(&a);
  items.insert(&b);
  items.insert(&c);
  items.insert(&d);
  // std::set<Item*> highest_profit = GetItemsMaxProfit(items, 7);
  // for (Item* i : highest_profit) std::cout << i->name << " ";
  // std::cout << std::endl;
  // highest_profit = GetItemsMaxProfit(items, 6);
  // for (Item* i : highest_profit) std::cout << i->name << " ";
  std::cout << GetMaxProfit(items, 7, Method::BOTTOM_UP);
  return 0;
};

int GetMaxProfit(std::set<Item*>& items, int capacity, Method m) {
  std::vector<int> profits;
  std::vector<int> weights;
  for (auto it = items.begin(); it != items.end(); ++it) {
    profits.push_back((*it)->value);
    weights.push_back((*it)->weight);
  }
  std::vector<std::vector<int>> dp(profits.size(),
                                   std::vector<int>(capacity + 1));
  switch (m) {
    case Method::BRUTE_FORCE:
      return GetMaxProfit(profits, weights, capacity, 0);
    case Method::MEMOIZE:
      return GetMaxProfitMemoize(profits, weights, capacity, 0, dp);
    case Method::BOTTOM_UP:
      return GetMaxProfitBottomUp(profits, weights, dp);
  }
  return 0;
};

int GetMaxProfit(std::vector<int>& profits, std::vector<int>& weights,
                 int capacity, size_t curr_index) {
  if (capacity <= 0 || curr_index >= profits.size()) return 0;
  int with = 0;
  if (capacity >= weights[curr_index])
    with = profits[curr_index] + GetMaxProfit(profits, weights,
                                              capacity - weights[curr_index],
                                              curr_index + 1);
  int without = GetMaxProfit(profits, weights, capacity, curr_index + 1);
  return std::max(with, without);
};

int GetMaxProfitMemoize(std::vector<int>& profits, std::vector<int>& weights,
                        int capacity, size_t curr_index,
                        std::vector<std::vector<int>>& dp) {
  if (capacity <= 0 || curr_index >= profits.size()) return 0;
  if (dp[curr_index][capacity] != 0) return dp[curr_index][capacity];
  int with = 0;
  if (capacity >= weights[curr_index])
    with = profits[curr_index] +
           GetMaxProfitMemoize(profits, weights, capacity - weights[curr_index],
                               curr_index + 1, dp);
  int without =
      GetMaxProfitMemoize(profits, weights, capacity, curr_index + 1, dp);
  dp[curr_index][capacity] = std::max(with, without);
  return dp[curr_index][capacity];
};

int GetMaxProfitBottomUp(std::vector<int>& profits, std::vector<int>& weights,
                         std::vector<std::vector<int>>& dp) {
  for (size_t i = 0; i < dp.size(); ++i) {
    for (size_t cap = 0; cap < dp[i].size(); ++cap) {
      if (i == 0) {
        dp[i][cap] = (size_t)weights[i] <= cap ? profits[i] : 0;
      } else {
        if ((size_t)weights[i] <= cap) {
          dp[i][cap] = profits[i] + dp[i - 1][cap - weights[i]];
        } else {
          dp[i][cap] = dp[i - 1][cap];
        }
      }
    }
  }
  return dp[dp.size() - 1][dp[0].size() - 1];
};

std::set<Item*> GetItemsMaxProfit(std::set<Item*>& items, int capacity) {
  std::list<Item*> selected;
  std::list<Item*> items_vector(items.begin(), items.end());
  std::list<Item*> highest_profit =
      GetItemsMaxProfit(items_vector, selected, capacity);
  return std::set<Item*>(highest_profit.begin(), highest_profit.end());
};

std::list<Item*> GetItemsMaxProfit(std::list<Item*>& items,
                                   std::list<Item*>& selected, int capacity) {
  if (items.size() == 0 || capacity == 0) return selected;
  Item* i = items.front();
  items.pop_front();
  std::list<Item*> with;
  if (i->weight <= capacity) {
    selected.push_back(i);
    with = GetItemsMaxProfit(items, selected, capacity - i->weight);
    selected.pop_back();
  } else {
    with = selected;
  }
  std::list<Item*> without = GetItemsMaxProfit(items, selected, capacity);
  items.push_front(i);
  return (TotalProfit(with) < TotalProfit(without)) ? without : with;
};

int TotalWeight(const std::list<Item*>& items) {
  int weight = 0;
  for (Item* i : items) weight += i->weight;
  return weight;
};

int TotalProfit(const std::list<Item*>& items) {
  int profit = 0;
  for (Item* i : items) profit += i->value;
  return profit;
};
