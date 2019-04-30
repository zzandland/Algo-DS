#include <iostream>
#include <vector>

enum class Method {
  BRUTE, MEM, BU
};

int Staircase(int n, Method m);
int Brute(int n);
int Memoize(int n, std::vector<int>& dp);
int BU(int n);

int main(void)
{
  Method b = Method::BRUTE;
  Method m = Method::MEM;
  Method bu = Method::BU;
  int n = 25;
  std::cout << Staircase(n, b) << ":" << Staircase(n, m) << ":" << Staircase(n, bu);
  return 0;
}

int Staircase(int n, Method m) {
  std::vector<int> dp(n + 1);
  switch (m) {
    case Method::BRUTE:
      return Brute(n);
    case Method::MEM:
      return Memoize(n, dp);
    case Method::BU:
      return BU(n);
  }
};

int Brute(int n) {
  if (n == 0) return 1;
  if (n < 0) return 0;
  return Brute(n - 1) + Brute(n - 2) + Brute(n - 3);
};

int Memoize(int n, std::vector<int>& dp) {
  if (n == 0) return 1;
  if (n < 0) return 0;
  if (dp[n] == 0)
    dp[n] = Brute(n - 1) + Brute(n - 2) + Brute(n - 3);
  return dp[n];
};

int BU(int n) {
  if (n < 3) return n;
  int a = 1, b = 1, c = 2;
  for (int i = 3; i <= n; ++i) {
    int tmp = a + b + c;
    a = b;
    b = c;
    c = tmp;
  }
  return c;
};
