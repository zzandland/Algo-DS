class Solution {
public:
    vector<int> tmp;
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        dfs(0, candidates, target, res);
        return res;
    }
    
    void dfs(int i, vector<int> &candidates, int n, vector<vector<int>> &res) {
        if (n < 0 || i == candidates.size()) return;
        if (n == 0) {
            vector<int> cpy = tmp;
            res.push_back(cpy);
            return;
        }
        tmp.push_back(candidates[i]);
        dfs(i, candidates, n - candidates[i], res);
        tmp.pop_back();
        dfs(i+1, candidates, n, res);
    }
};