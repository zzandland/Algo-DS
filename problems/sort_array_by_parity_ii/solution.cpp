class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        size_t e = 0, o = 1, N = nums.size();
        while (e < N && o < N) {
            if (nums[e] % 2 == 0) e += 2;
            else if (nums[o] % 2 == 1) o += 2;
            else {
                swap(nums[e], nums[o]);
                e += 2;
                o += 2;
            }
            
        }
        return nums;
    }
};