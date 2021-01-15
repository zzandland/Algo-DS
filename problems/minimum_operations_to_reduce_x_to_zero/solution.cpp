class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int t = -x;
        for (int n : nums) t += n;
        if (t < 0) return -1;
        if (t == 0) return nums.size();
        int run, res;
        run = res = 0;
        for (int l = 0, r = 0; r < nums.size();) {
            run += nums[r++];
            while (run > t) run -= nums[l++];
            if (run == t) res = max(res, r-l);
        }
        return (res == 0) ? -1 : nums.size() - res;
    }
};