#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int HouseThief(std::vector<int>& houses, Method m);
int Brute(std::vector<int>& houses, size_t i);
int Memoize(std::vector<int>& houses, size_t i, std::vector<int>& dp);
int BU(std::vector<int>& houses);

int main(void) {
  std::vector<int> h1 = {2, 5, 1, 3, 6, 2, 4};
  std::vector<int> h2 = {2, 10, 14, 8, 1, 2, 8, 15, 3, 10, 7, 6, 6, 6, 23, 1};
  Method m = Method::MEM;
  std::cout << HouseThief(h1, m) << ":" << HouseThief(h2, m);
  return 0;
}

int HouseThief(std::vector<int>& houses, Method m) {
  std::vector<int> dp(houses.size() + 1);
  switch (m) {
    case Method::BRUTE:
      return Brute(houses, 0);
    case Method::MEM:
      return Memoize(houses, 0, dp);
    case Method::BU:
      return BU(houses);
  }
}

int Brute(std::vector<int>& houses, size_t i) {
  if (i >= houses.size()) return 0;
  return std::max(houses[i] + Brute(houses, i + 2), Brute(houses, i + 1));
}

int Memoize(std::vector<int>& houses, size_t i, std::vector<int>& dp) {
  if (i >= houses.size()) return 0;
  if (dp[i] == 0)
    dp[i] = std::max(houses[i] + Memoize(houses, i + 2, dp),
                     Memoize(houses, i + 1, dp));
  return dp[i];
}

int BU(std::vector<int>& houses) {
  int val1 = houses[0];
  int val2 = std::max(val1, houses[1]);
  for (size_t i = 2; i < houses.size(); ++i) {
    int tmp = std::max(val2, houses[i] + val1);
    val1 = val2;
    val2 = tmp;
  }
  return val2;
}
