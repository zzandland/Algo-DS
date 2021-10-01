class Solution {
public:
    int target_;
    
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k > 0) return false;
        target_ = sum / k;
        vector<int> sums(k, 0);
        sort(nums.rbegin(), nums.rend());
        return dfs(nums, k, 0, sums);
    }
    
    bool dfs(vector<int> &nums, int k, int i, vector<int> &sums) {
        int N = nums.size();
        if (i == N) {
            for (int j = 0; j < k; ++j) {
                if (sums[j] != target_) return false;
            }
            return true;
        }
        for (int j = 0; j < k; ++j) {
            if (sums[j] + nums[i] > target_) continue;
            sums[j] += nums[i];
            if (dfs(nums, k, i+1, sums)) return true;
            sums[j] -= nums[i];
        }
        return false;
    }
};