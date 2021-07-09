class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp;
        for (int n : nums) {
            int j = bs(dp, n);
            if (j == dp.size()) dp.push_back(n);
            else if (n < dp[j]) dp[j] = n;
        }
        return dp.size();
    }
    
    int bs(vector<int>& dp, int n) {
        int l = 0, r = dp.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (dp[m] < n) l = m + 1;
            else r = m;
        }
        return l;
    }
};