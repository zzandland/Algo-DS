import java.util.*;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
      List<Integer> output = new ArrayList<Integer>();
      if (matrix.length == 0) return output;
      int x, vOffset, hOffset;
      for (int layer = 0; layer <= matrix.length / 2; layer++) {
        x = layer;
        vOffset = matrix.length - layer - 1;
        hOffset = matrix[0].length - layer - 1;
        if (vOffset == x  && hOffset == x) {
          output.add(matrix[x][x]);
          return output;
        }
        if ((vOffset == 0 || hOffset == 0) && layer > 0) return output; 
        if (matrix.length * matrix[0].length == output.size()) return output;
        for (int a = x; a < hOffset; a++) {
          output.add(matrix[x][a]);
        }
        for (int b = x; b < vOffset; b++) {
          output.add(matrix[b][hOffset]);
        }
        if (vOffset == layer) {
          output.add(matrix[x][hOffset]);
          return output;
        }
        if (hOffset == layer) {
          output.add(matrix[vOffset][x]);
          return output;
        }
        for (int c = hOffset; c > x; c--) {
          output.add(matrix[vOffset][c]);
        }
        for (int d = vOffset; d > x; d--) {
          output.add(matrix[d][x]);
        }
      } 
      return output;
    }
}