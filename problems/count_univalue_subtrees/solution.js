/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var countUnivalSubtrees = function(root) {
  if (!root) {
    return 0;
  }
  var output = 0;
  var innerFunc = (node) => {
    if (node.left) {
      var left = innerFunc(node.left);
    }
    if (node.right) {
      var right = innerFunc(node.right);
    }
    if (
      (!node.left && !node.right) ||
      (node.left && !node.right && left === node.val) ||
      (!node.left && node.right && right === node.val) ||
      (node.left && node.right && left === node.val && right === node.val) 
    ) {
      output++;
      return node.val;
    }
  }
  innerFunc(root);
  return output;
};