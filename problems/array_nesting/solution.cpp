class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int res = 0, N = nums.size();
        vector<bool> seen(N);
        for (int i = 0; i < N; ++i) {
            int tmp = 0, j = i;
            while (!seen[j]) {
                seen[j] = true;
                ++tmp;
                j = nums[j];
            }
            res = max(res, tmp);
            if (res == N) break;
        }
        return res;
    }
};