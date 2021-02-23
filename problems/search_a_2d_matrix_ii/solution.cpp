class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int y = matrix.size()-1, x = 0;
        while (y >= 0 && x < matrix[0].size()) {
            int val = matrix[y][x];
            if (val == target) return true;
            if (val > target) y--;
            if (val < target) x++;
        }
        return false;
    }
};