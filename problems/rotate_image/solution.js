/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
  if (matrix.length === 0 || matrix.length !== matrix[0].length) return false;
  for (var layer = 0; layer < matrix.length / 2; layer++) {
    var first = layer;
    var last = matrix.length - 1 - first;
    for (var i = first; i < last; i++) {
      var offset = i - first;
      var top = matrix[first][i];
      matrix[first][i] = matrix[last - offset][first];
      matrix[last - offset][first] = matrix[last][last - offset];
      matrix[last][last - offset] = matrix[i][last];
      matrix[i][last] = top;
    }
  }
};