class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0, tmp = 0;
        for (int n : nums) {
            if (n == 1) {
                ++tmp;
            } else {
                res = max(res, tmp);
                tmp = 0;
            }
        }
        return max(res, tmp);
    }
};