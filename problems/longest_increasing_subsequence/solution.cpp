class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> res;
        for (int n : nums) {
            int i = bs(res, n);
            if (i == res.size()) {
                res.push_back(n);
            } else {
                res[i] = min(res[i], n);
            }
        }
        return res.size();
    }
    
    int bs(vector<int> &nums, int n) {
        int l = 0, r = nums.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] >= n) r = m;
            else l = m + 1;
        }
        return l;
    }
};