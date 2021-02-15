class Solution {
public:
    using p = pair<int, int>;
    
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        auto cmp = [&](p &a, p &b) -> bool {
            if (a.second == b.second) return a.first > b.first;
            return a.second > b.second;
        };
        vector<p> q;
        for (int i = 0; i < mat.size(); ++i)
            q.push_back({i, count(mat[i].begin(), mat[i].end(), 1)});
        
        make_heap(q.begin(), q.end(), cmp);
        vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(q.front().first);
            pop_heap(q.begin(), q.end(), cmp);
            q.pop_back();
        }
        return res;
    }
};