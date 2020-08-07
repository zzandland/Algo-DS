class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int M = mat.size(), N = mat[0].size();
        vector<pair<int, int>> arr;
        for (int y = M-1; y >= 0; --y) arr.push_back({y, 0});
        for (int x = 0; x < N; ++x) arr.push_back({0, x});
        
        for (auto [r, c]: arr) {
            int y = r, x = c;
            vector<int> tmp;
            while (y < M && x < N) tmp.push_back(mat[y++][x++]);
            sort(tmp.begin(), tmp.end());
            y = r, x = c;
            for (int val: tmp) {
                mat[y++][x++] = val;
            }
        }
        return mat;
    }
};