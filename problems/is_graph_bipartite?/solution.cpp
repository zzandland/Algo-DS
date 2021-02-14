class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        queue<int> q;
        vector<int> seen(graph.size());
        for (int i = 0; i < graph.size(); ++i) {
            if (seen[i] == 0 && graph[i].size()) {
                q.push(i);
                // 0 not visited 1 for red 2 for blue
                seen[i] = 1;
                while (!q.empty()) {
                    int n = q.front();
                    q.pop();
                    for (int nn : graph[n]) {
                        if (seen[nn] == seen[n]) return false;
                        if (seen[nn] == 0) {
                            seen[nn] = seen[n] == 1 ? 2 : 1;
                            q.push(nn);
                        }
                    }
                }
            } 
        }
        return true;
    }
};