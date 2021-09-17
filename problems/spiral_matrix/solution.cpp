class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int R = matrix.size(), C = matrix[0].size();
        pair<int, int> dir[] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<vector<bool>> seen(R, vector<bool>(C));
        vector<int> res(R*C);
        int y = 0, x = 0, d = 0;
        for (int i = 0; i < R*C; ++i) {
            res[i] = matrix[y][x];
            seen[y][x] = true;
            bool good = false;
            int ny, nx, t = d;
            while (!good) {
                ny = y + dir[d].first, nx = x + dir[d].second;
                if (0 <= ny && ny < R && 0 <= nx && nx < C && !seen[ny][nx]) {
                    good = true;
                } else {
                    d = (d + 1) % 4;
                    if (t == d) break;
                }
            }
            y = ny, x = nx;
        }
        return res;
    }
};