class Solution {
public:
    const vector<int> dir = {-1, 0, 1, 0, -1};
    
    int cutOffTree(vector<vector<int>>& forest) {
        if (!forest.size()) return -1;
        
        vector<pair<int, int>> trees;
        for (int y = 0; y < forest.size(); ++y) {
            for (int x = 0; x < forest[y].size(); ++x) {
                if (forest[y][x] > 1) trees.push_back({y, x});
            }
        }
        
        sort(trees.begin(), trees.end(), [&](auto& a, auto& b) {
            return forest[a.first][a.second] < forest[b.first][b.second];
        });
        
        int res = 0, y = 0, x = 0;
        for (auto [ty, tx]: trees) {
            int d = getDist(y, x, ty, tx, forest);
            if (d < 0) return -1;
            res += d;
            y = ty;
            x = tx;
        }
        
        return res;
    }
    
    int getDist(int sy, int sx, int ty, int tx, vector<vector<int>>& forest) {
        int m = forest.size(), n = forest[0].size();
        vector<vector<int>> seen(m, vector<int>(n, 0));
        queue<pair<int, int>> q;
        seen[sy][sx] = 1;
        q.emplace(sy, sx);
        int res = 0;
        
        while (!q.empty()) {
            int len = q.size();
            for (int j = 0; j < len; ++j) {
                auto [y, x] = q.front();
                q.pop();
                if (y == ty && x == tx) return res;
                for (int i = 1; i < dir.size(); ++i) {
                    int ny = y + dir[i-1], nx = x + dir[i];
                    if (0 <= ny && ny < m && 0 <= nx && nx < n && forest[ny][nx] > 0 && !seen[ny][nx]) {
                        seen[ny][nx] = 1;
                        q.emplace(ny, nx);
                    }
                }
            }
            ++res;
        }
        
        return -1;
    }
};