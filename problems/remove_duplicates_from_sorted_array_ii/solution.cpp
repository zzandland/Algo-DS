class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int prev = 0, freq = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[prev]) {
                nums[++prev] = nums[i];
                freq = 1;
            } else if (nums[i] == nums[prev] && freq + 1 < 3) {
                nums[++prev] = nums[i];
                freq++;
            }
        }
        return prev + 1;
    }
};