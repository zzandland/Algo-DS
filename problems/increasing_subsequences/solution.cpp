class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(res, tmp, nums, 0);
        return res;
    }
    
    void dfs(vector<vector<int>> &res, vector<int> &tmp, vector<int> &nums, int pos) {
        if (tmp.size() > 1) {
            res.push_back(tmp);
        }
        unordered_set<int> seen;
        for (int i = pos; i < nums.size(); ++i) {
            int n = nums[i];
            if ((tmp.empty() || tmp.back() <= n) && !seen.count(n)) {
                tmp.push_back(n);
                dfs(res, tmp, nums, i + 1);
                tmp.pop_back();
                seen.insert(n);
            }
        }
    }
};