/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[][]}
 */
var printTree = function(root) {
  var output = [];
  var maxLevel = 0;
  var checkMaxLevel = (node, level) => {
    if (node.left) {
      var left = Math.max(checkMaxLevel(node.left, level + 1), level);
    }
    if (node.right) {
      var right = Math.max(checkMaxLevel(node.right, level + 1), level);
    }
    return Math.max(level, (left || 0), (right || 0));
  }
  
  var maxLevel = checkMaxLevel(root, 0);
  var numOfCol = 0;
  for (let i = 0; i <= maxLevel; i++) {
    numOfCol += Math.pow(2, i);
  }
  
  var innerFunc = (node, level, index, interval) => {
    if (!output[level]) {
      output[level] = [];
      for (var i = 0; i < numOfCol; i++) {
        output[level].push('');
      }
    }
    output[level][index] += node.val;
    if (node.left) {
      innerFunc(node.left, level + 1, index - interval, interval / 2);
    }
    if (node.right) {
      innerFunc(node.right, level + 1, index + interval, interval / 2);
    }
  }
  innerFunc(root, 0, Math.floor(numOfCol / 2), Math.ceil(numOfCol / 4));
  return output;
};