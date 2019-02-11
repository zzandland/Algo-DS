class Solution {
  public void rotate(int[][] matrix) {
    int start, end;
    for (int i = 0; i < matrix.length / 2; i++) {
      start = i;
      end = matrix.length - 1 - i;
      for (int j = start; j < end; j++) {
        int offset = end - j + start;
        int tmp = matrix[start][j];
        matrix[start][j] = matrix[offset][start];
        matrix[offset][start] = matrix[end][offset];
        matrix[end][offset] = matrix[j][end];
        matrix[j][end] = tmp;
      }
    }
  }
}