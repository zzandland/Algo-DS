class Solution {
public:
    vector<unordered_set<int>> tree;
    vector<int> count, res;
    int N;
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        N = n;
        tree.resize(N);
        count.assign(N, 1);
        res.assign(N, 0);
        for (auto edge : edges) {
            tree[edge[0]].insert(edge[1]);
            tree[edge[1]].insert(edge[0]);
        }
        res[0] = dfs(0, -1);
        dfs2(0, -1);
        return res;
    }
    
    int dfs(int n, int p) {
        int res = 0;
        for (int nn : tree[n]) {
            if (nn == p) continue;
            int sum = dfs(nn, n);
            count[n] += count[nn];
            res += sum + count[nn];
        }
        return res;
    }
    
    void dfs2(int n, int p) {
        for (int nn : tree[n]) {
            if (nn == p) continue;
            res[nn] = res[n] - count[nn] + (N - count[nn]);
            dfs2(nn, n);
        }
    }
};