#include <iostream>
#include <vector>

int TripleStep(int n);
int TripleStepMem(int n);
int TripleStepMem(int n, std::vector<int>& dp);
int BU(int n);

int main(void) {
  std::cout << TripleStep(10) << ":" << TripleStepMem(10) << ":" << BU(10);
  return 0;
}

int TripleStep(int n) {
  if (n < 0) return 0;
  if (n == 0) return 1;
  return TripleStep(n - 1) + TripleStep(n - 2) + TripleStep(n - 3);
}

int TripleStepMem(int n) {
  std::vector<int> dp(n + 1);
  return TripleStepMem(n, dp);
}

int TripleStepMem(int n, std::vector<int>& dp) {
  if (n < 0) return 0;
  if (n == 0) return 1;
  if (dp[n] == 0)
    dp[n] = TripleStepMem(n - 1, dp) + TripleStepMem(n - 2, dp) +
            TripleStepMem(n - 3, dp);
  return dp[n];
}

int BU(int n) {
  if (n < 3) return n;
  std::vector<int> dp(n + 1);
  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 2;
  for (int i = 3; i <= n; ++i) dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
  return dp[n];
}
