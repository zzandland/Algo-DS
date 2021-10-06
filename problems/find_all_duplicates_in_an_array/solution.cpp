class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        int i = 0, N = nums.size();
        while (i < N) {
            int j = nums[i] - 1;
            if (i != j && nums[j] != j + 1) {
                swap(nums[i], nums[j]);
            } else {
                ++i;
            }
        }
        for (int i = 0; i < N; ++i) {
            if (nums[i] != i+1) {
                res.push_back(nums[i]);
            }
        }
        return res;
    }
};