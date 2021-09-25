typedef struct {
    int y, x, k;
} P;

class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        if (grid[0][0] == 1 && k < 1) return -1;
        int R = grid.size(), C = grid[0].size();
        queue<P> q;
        array<int, 5> dirs {-1, 0, 1, 0, -1};
        vector<vector<int>> seen(R, vector<int>(C, -1));
        q.push({0, 0, k - int(grid[0][0] == 1)});
        seen[0][0] = q.front().k;
        int res = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                P p = q.front();
                q.pop();
                if (p.y == R-1 && p.x == C-1) return res;
                for (int i = 0; i < 4; ++i) {
                    int ny = p.y + dirs[i], nx = p.x + dirs[i+1];
                    if (0 <= ny && ny < R && 0 <= nx && nx < C) {
                        if (grid[ny][nx] == 1 && p.k == 0) continue;
                        int nk = p.k - int(grid[ny][nx] == 1);
                        if (seen[ny][nx] < nk) {
                            seen[ny][nx] = nk;
                            q.push({ny, nx, nk});
                        }
                    }
                }
            }
            ++res;
        }
        return -1;
    }
};