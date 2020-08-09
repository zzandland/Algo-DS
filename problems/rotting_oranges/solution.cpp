class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if (!grid.size()) return 0;       
        int M = grid.size(), N = grid[0].size();

        // find pos of rotten O(grid)
        queue<pair<int, int>> q;
        int fresh = 0;
        for (int y = 0; y < M; ++y) {
            for(int x = 0; x < N; ++x) {
                if (grid[y][x] == 2) q.emplace(y, x);
                else if (grid[y][x] == 1) ++fresh;
            }
        }
        
        // BFS O(grid)
        int time = 0;
        pair<int, int> dirs[4] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.empty()) {
            if (!fresh) return time;
            ++time;
            int len = q.size();
            for (int i = 0; i < len; ++i) {
                auto [y, x] = q.front();
                q.pop();
                for (auto [r, c]: dirs) {
                    int ny = y+r, nx = x+c;
                    if (0 <= ny && ny < M && 0 <= nx && nx < N && grid[ny][nx] == 1) {
                        grid[ny][nx] = 2;
                        q.emplace(ny, nx);
                        --fresh;
                    }
                }
            }
        }
        return fresh ? -1 : time;
    }
};