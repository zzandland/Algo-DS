/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
  var output = [];
  var queue = [root];
  var level = -1;
  var node, length;
  if (root === null) {
    return [];
  }
  while (queue.length !== 0) {
    level += 1;
    length = queue.length;
    for (var i = 0 ; i < length; i++) {
      if (output[level] === undefined) {
        output[level] = [];
      }
      node = queue.pop();
      if (node.left) {
        queue.unshift(node.left);
      }  
      if (node.right) {
        queue.unshift(node.right);
      }
      output[level].push(node.val);
    }
    if (level % 2 === 1) {
      output[level] = output[level].reverse();
    }
  }
  return output;
};