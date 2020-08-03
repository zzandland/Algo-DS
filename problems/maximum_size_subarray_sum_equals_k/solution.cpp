class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        seen[0] = -1;
        int run = 0, res = 0;
        for (int i = 0; i < nums.size(); ++i) {
            run += nums[i];
            if (seen.count(run-k)) res = max(res, i - seen[run-k]);
            if (!seen.count(run)) seen[run] = i;
        }
        return res;
    }
};