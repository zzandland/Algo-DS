/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
  debugger;
  if (matrix.length === 0) {
    return false;
  }
  var left = 0; 
  var right = matrix.length - 1;
  var row;
  while (right > left) {
    var mid = left + Math.floor((right - left) / 2);
    if (matrix[mid][0] <= target && matrix[mid][matrix[mid].length - 1] >= target) {
      row = matrix[mid];
      break;
    }
    if (matrix[mid][0] > target) {
      right = mid - 1;
    } else if (matrix[mid][matrix[mid].length - 1] < target) {
      left = mid + 1;
    }
  }
  if (!row) {
    row = matrix[left];
  }
  var rowLeft = 0;
  var rowRight = row.length - 1;
  while (rowRight > rowLeft) {
    var rowMid = rowLeft + Math.floor((rowRight - rowLeft) / 2);
    if (row[rowMid] === target) {
      return true;
    }
    if (row[rowMid] < target) {
      rowLeft = rowMid + 1;
    } else if (row[rowMid] > target) {
      rowRight = rowMid - 1;
    }
  }
  return row[rowLeft] === target;
};
