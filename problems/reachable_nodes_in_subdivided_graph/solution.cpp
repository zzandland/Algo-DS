class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        unordered_map<int, unordered_map<int, int>> em;
        unordered_map<int, int> seen;
        for (vector<int> e : edges) {
            int a = e[0], b = e[1], d = e[2];
            em[a][b] = d;
            em[b][a] = d;
        }
        priority_queue<pair<int, int>> q;
        q.push({maxMoves, 0});
        while (!q.empty()) {
            auto [moves, n] = q.top();
            q.pop();
            if (seen.count(n) || moves < 0) continue;
            seen[n] = moves;
            for (auto [nn, d] : em[n]) {
                if (!seen.count(nn)) {
                    q.push({moves - d - 1, nn});
                }
            }
        }
        int res = seen.size();
        for (vector<int> e : edges) {
            int a = e[0], b = e[1];
            res += min(seen[a] + seen[b], em[a][b]);
        }
        return res;
    }
};