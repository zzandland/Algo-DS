class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int N = nums.size();
        vector<vector<int>> res;
        for (int i = 0; i < N; ++i) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int l = i+1, r = N-1;
            while (l < r) {
                if (l > i+1 && nums[l] == nums[l-1]) {
                    ++l;
                    continue;
                }
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    res.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    ++l;
                } else if (sum < 0) {
                    ++l;
                } else {
                    --r;
                }
            }
        }
        return res;
    }
};