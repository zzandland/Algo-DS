int helper(int n, int *dp){
  if (n <= 0) {
    return n == 0 ? 1 : 0;
  }
  if (!dp[n]) {
    dp[n] = helper(n - 1, dp) + helper(n - 2, dp);
  }
  return dp[n];
};

int climbStairs(int n) {
  int dp[10000] = { 0 }; 
  return helper(n, dp);
}