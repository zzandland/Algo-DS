class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int prev = -nums.size() - 1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                if (i - prev < k + 1) return false;
                prev = i;
            }
        }
        return true;
    }
};