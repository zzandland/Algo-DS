typedef pair<int, int> P;

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, zeros = 0, res = 0;
        for (int r = 0; r < nums.size(); ++r) {
            zeros += nums[r] == 0 ? 1 : 0;
            while (zeros > k) {
                zeros -= nums[l] == 0 ? 1 : 0;
                ++l;
            } 
            res = max(res, r - l + 1);
        }
        return res;
    }
};