class Solution {
public:
    int jump(vector<int>& nums) {
        int N = nums.size();
        if (N < 2) return 0;
        int lv, mx;
        lv = mx = 0;
        for (int i = 0; i < nums.size();) {
            ++lv;
            int nxt = 0;
            for (; i <= mx; ++i) {
                nxt = max(nxt, i + nums[i]);
                if (nxt >= nums.size() - 1) return lv;
            }
            mx = nxt;
        }
        return -1;
    }
};