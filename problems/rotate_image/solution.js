/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    N = matrix.length;
    for (let i = 0; i < Math.floor(N / 2); ++i) {
        for (let j = i; j < N - i - 1; ++j) {
            let offset = N-1-i;
            let tmp = matrix[i][j];
            matrix[i][j] = matrix[offset-j+i][i];
            matrix[offset-j+i][i] = matrix[offset][offset-j+i];
            matrix[offset][offset-j+i] = matrix[j][offset];
            matrix[j][offset] = tmp;
        }
    }
};