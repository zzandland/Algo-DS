#include <iostream>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int Fibonacci(int n, Method m);
int Brute(int n);
int Memoize(int n, std::vector<int>& dp);
int BU(int n, std::vector<int>& dp);

int main(void) {
  Method m = Method::BU;
  std::cout << Fibonacci(15, m);
  return 0;
}

int Fibonacci(int n, Method m) {
      std::vector<int> dp(n + 1);
  switch (m) {
    case Method::BRUTE:
      return Brute(n);
    case Method::MEM:
      return Memoize(n, dp);
    case Method::BU:
      return BU(n, dp);      
  }
};

int Brute(int n) {
  if (n == 0 || n == 1) return 1;
  return Brute(n - 1) + Brute(n - 2);
};

int Memoize(int n, std::vector<int>& dp) {
  if (n == 0 || n == 1) return 1;
  if (dp[n] != 0) return dp[n];
  dp[n] = Memoize(n - 1, dp) + Memoize(n - 2, dp);
  return dp[n];
};

int BU(int n, std::vector<int>& dp) {
  if (n < 2) return n;
  int first = 1, second = 1;
  for (int i = 2; i <= n; i += 2) {
    first += second;
    second += first;
  }
  return second;
}
