class Solution {
public:
    int bs_left(vector<int>& nums, int target) {
        int l = 0
          , r = nums.size()
          , m;
        while (l < r) {
            m = l + (r - l) / 2;
            if (nums[m] < target)
                l = m + 1;
            else 
                r = m;
        }
        return l;
    }
    
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = bs_left(nums, target)
          , r = bs_left(nums, target + 1) - 1;
        if (!nums.size() || l == nums.size() || nums[l] != target) return {-1, -1};
        return {l, r};
    }
};