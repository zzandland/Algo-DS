class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> q;
        q.push_back(vector<int>());
        for (auto num: nums) {
            vector<vector<int>> nq;
            for (auto perm: q) {
                for (int i = 0; i <= perm.size(); ++i) {
                    vector<int> cpy = perm;
                    cpy.insert(cpy.begin()+i, num);
                    nq.push_back(cpy);
                }
            }
            q = nq;
        }
        return q;
    }
};