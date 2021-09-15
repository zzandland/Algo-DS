class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int R = mat.size(), C = mat[0].size();
        vector<vector<bool>> seen(R, vector<bool>(C, false));
        queue<pair<int, int>> q;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (mat[i][j] == 0) {
                    q.push({i, j});
                    seen[i][j] = true;
                }
            }
        }
        int c = 0;
        vector<int> dir{-1, 0, 1, 0, -1};
        while (!q.empty()) {
            int len = q.size();
            for (int i = 0; i < len; ++i) {
                auto [y, x] = q.front();
                mat[y][x] = c;
                q.pop();
                for (int j = 0; j < 4; ++j) {
                    int ny = y + dir[j], nx = x + dir[j+1];
                    if (0 <= ny && ny < R && 0 <= nx && nx < C) {
                        if (!seen[ny][nx]) {
                            seen[ny][nx] = true;
                            q.push({ny, nx});
                        }
                    }
                }
            }
            ++c;
        }
        return mat;
    }
};