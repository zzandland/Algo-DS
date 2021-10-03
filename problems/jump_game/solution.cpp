class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() < 2) return true;
        int possible = 0;
        for (int i = 0; i < nums.size(); ++i) {
            possible = max(possible, i + nums[i]);
            if (possible >= nums.size() - 1) return true;
            if (i == possible) return false;
        }
        return possible >= nums.size() - 1;
    }
};