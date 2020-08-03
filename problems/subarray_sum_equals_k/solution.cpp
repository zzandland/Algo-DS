class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        seen[0] = 1;
        int run = 0, res = 0;
        for (int n: nums) {
            run += n;
            res += seen[run-k];
            seen[run] += 1;
        }
        return res;
    }
};