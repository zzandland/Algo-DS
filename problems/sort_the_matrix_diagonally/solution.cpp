class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        if (!mat.size() || !mat[0].size()) return mat;
        int R = mat.size(), C = mat[0].size();
        
        vector<int> tmp;
        for (int x = C-1; x >= 0; --x) {
            tmp.clear();
            for (int y = 0; y < R && y+x < C; ++y) tmp.push_back(mat[y][y+x]);
            sort(tmp.begin(), tmp.end());
            for (int y = 0, i = 0; y < R && y+x < C; ++y, ++i) mat[y][y+x] = tmp[i];
        }
        
        for (int y = 1; y < R; ++y) {
            tmp.clear();
            for (int x = 0; x < C && y+x < R; ++x) tmp.push_back(mat[y+x][x]);
            sort(tmp.begin(), tmp.end());
            for (int x = 0, i = 0; x < C && y+x < R; ++x, ++i) mat[y+x][x] = tmp[i];
        }
        return mat;
    }
};