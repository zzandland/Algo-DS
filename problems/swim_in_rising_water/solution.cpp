typedef struct {
    int y, x, h;
} Coord;

class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        auto cmp = [&](Coord &a, Coord &b) {
            return a.h > b.h;
        };
        int Y = grid.size(), X = grid[0].size();
        priority_queue<Coord, vector<Coord>, decltype(cmp)> pq(cmp);
        vector<vector<bool>> seen(Y, vector<bool>(X, false));
        int dir[] = {-1, 0, 1, 0, -1};
        pq.push({0, 0, grid[0][0]});
        seen[0][0] = true;
        int res = 0;
        while (!pq.empty()) {
            auto [y, x, h] = pq.top();
            res = max(res, h);
            if (y == Y-1 && x == X-1) break;
            pq.pop();
            for (int i = 0; i < 4; ++i) {
                int ny = y + dir[i], nx = x + dir[i+1];
                if (0 <= ny && ny < Y && 0 <= nx && nx < X && !seen[ny][nx]) {
                    seen[ny][nx] = true;
                    pq.push({ny, nx, grid[ny][nx]});
                }
            }
        }
        return res;
    }
};