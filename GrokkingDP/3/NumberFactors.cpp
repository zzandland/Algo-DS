#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int NumberFactors(int n, Method m);
int Brute(int n);
int Memoize(int n, std::vector<int>& dp);
int BU(int n);

int main(void) {
  int n = 35;
  std::cout << NumberFactors(n, Method::BRUTE) << ":"
            << NumberFactors(n, Method::MEM) << ":"
            << NumberFactors(n, Method::BU);
  return 0;
}

int NumberFactors(int n, Method m) {
  std::vector<int> dp(n + 1);
  switch (m) {
    case Method::BRUTE:
      return Brute(n);
    case Method::MEM:
      return Memoize(n, dp);
    case Method::BU:
      return BU(n);
  }
}

int Brute(int n) {
  if (n == 0) return 1;
  if (n < 0) return 0;
  return Brute(n - 1) + Brute(n - 3) + Brute(n - 4);
}

int Memoize(int n, std::vector<int>& dp) {
  if (n == 0) return 1;
  if (n < 0) return 0;
  if (dp[n] == 0)
    dp[n] = Memoize(n - 1, dp) + Memoize(n - 3, dp) + Memoize(n - 4, dp);
  return dp[n];
}

int BU(int n) {
  if (n == 0 || n == 1 || n == 2)
    return 1;
  else if (n == 3)
    return 2;
  int a = 1, b = 1, c = 1, d = 2;
  for (int i = 4; i <= n; ++i) {
    int tmp = a + b + d;
    a = b;
    b = c;
    c = d;
    d = tmp;
  }
  return d;
}
