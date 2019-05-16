class Solution {
public:
  void rotate(vector<vector<int>>& matrix) {
    int m_len = matrix.size();
    for (int i = 0; i < m_len / 2; ++i) {
      int offset = m_len - 1;
      for (int j = i; j < offset - i; ++j) {
        int tmp = matrix[i][j];
        matrix[i][j] = matrix[offset - j][i];
        matrix[offset - j][i] = matrix[offset - i][offset - j];
        matrix[offset - i][offset - j] = matrix[j][offset - i];
        matrix[j][offset - i] = tmp;
      }
    }
  }
};