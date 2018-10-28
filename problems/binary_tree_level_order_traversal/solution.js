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
var levelOrder = function(root) {
  if (!root) {
    return [];
  }
  var output = [];
  var queue = [root];
  var level = -1;
  var length;
  var node;
  while (queue.length) {
    level += 1;
    output[level] = [];
    length = queue.length;
    for (var i = 0; i < length; i++) {
      node = queue.pop();
      output[level].push(node.val);
      if (node.left) {
        queue.unshift(node.left);
      }
      if (node.right) {
        queue.unshift(node.right);
      }
    }
  }
  return output;
};