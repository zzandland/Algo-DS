class NumMatrix {
public:
    NumMatrix(vector<vector<int>>& matrix)
        : mt(matrix.size() + 1, vector<int>(matrix[0].size() + 1)) {
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix[0].size(); ++j) {
                mt[i+1][j+1] = matrix[i][j] + mt[i][j+1] +
                    mt[i+1][j] - mt[i][j];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return mt[row2+1][col2+1] - mt[row2+1][col1] -
            mt[row1][col2+1] + mt[row1][col1];
    }
private:
    vector<vector<int>> mt;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */