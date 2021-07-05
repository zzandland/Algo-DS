class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size(), n = mat[0].size();
        if (m*n != r*c) return mat;
        vector<vector<int>> res(r, vector<int>(c));
        for (int i = 0, k = 0, l = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j, ++l) {
                if (l == c)  l = 0, ++k;
                res[k][l] = mat[i][j];
            }
        }
        return res;
    }
};