class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        auto cmp = [&](vector<int> &a, vector<int> &b) {
            return a[a.size()-1] < b[b.size()-1];
        };
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);
        for (auto row : matrix) {
            pq.push(row);
        }
        int cur = matrix[0].size() * matrix.size(), res = 0;
        while (cur-- >= k) {
            vector<int> v = pq.top();
            pq.pop();
            res = v[v.size()-1];
            v.pop_back();
            if (v.size() > 0) pq.push(v);
        }
        return res;
    }
};