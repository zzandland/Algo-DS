class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        unsigned int dp[target+1];
        dp[0] = 1;
        for (int i = 1; i <= target; ++i) {
            dp[i] = 0;
            for (auto &n : nums) {
                if (n <= i) {
                    dp[i] += dp[i - n];
                }
            }
        }
        return dp[target];
    }
};