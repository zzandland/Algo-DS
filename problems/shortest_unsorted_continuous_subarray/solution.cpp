class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> mins;
        vector<int> maxs;
        int t = INT_MIN;
        for (int n : nums) {
            t = max(t, n);
            maxs.push_back(t);
        }
        t = INT_MAX;
        for (int i = nums.size()-1; i >= 0; --i) {
            t = min(t, nums[i]);
            mins.push_back(t);
        }
        // yennyga coding haejumyun joa
        // sudokuga joa
        int mx = 0, mn = nums.size();
        for (int i = 0; i < nums.size(); ++i) {
            if (mins[nums.size()-1-i] != maxs[i]) {
                mn = min(mn, i);
                mx = max(mx, i);
            }
        }
        return mn == nums.size() ? 0 : mx - mn + 1;
    }
};