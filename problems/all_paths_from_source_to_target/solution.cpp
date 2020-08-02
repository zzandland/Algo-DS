class Solution {
public:
    vector<int> tmp;
    unordered_set<int> seen;    
    vector<vector<int>> res;

    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        dfs(0, graph.size()-1, graph);
        return res;
    }
    
    void dfs(int n, int dest, vector<vector<int>>& graph) {
        if (n == dest) {
            vector<int> copy = tmp;
            copy.push_back(n);
            res.push_back(copy);
            return;
        }
        if (seen.count(n)) return;
        seen.emplace(n);
        tmp.push_back(n);
        for (int nn: graph[n]) dfs(nn, dest, graph);
        seen.erase(n);
        tmp.pop_back();
    }
};