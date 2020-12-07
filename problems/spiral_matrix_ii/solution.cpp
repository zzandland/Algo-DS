class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n, vector<int>(n, -1));
        int y, x, d, ny, nx;
        y = x = d = 0;
        pair<int, int> dir[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int i = 1; i <= n*n; ++i) {
            res[y][x] = i;
            ny = y + dir[d].first;
            nx = x + dir[d].second;
            if (0 > ny || ny >= n || 0 > nx || nx >= n || res[ny][nx] != -1) {
                d = (d+1) % 4;
                ny = y + dir[d].first;
                nx = x + dir[d].second;
            }
            y = ny;
            x = nx;
        }
        return res;
    }
};