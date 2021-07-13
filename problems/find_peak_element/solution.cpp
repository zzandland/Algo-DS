class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r - 1) {
            int m = l + (r - l) / 2;
            if (nums[m-1] < nums[m] && nums[m] > nums[m+1]) {
                return m;
            } else if (nums[m-1] < nums[m] && nums[m+1]) {
                l = m;
            } else {
                r = m;
            }
        }
        return nums[l] < nums[r] ? r : l;
    }
};