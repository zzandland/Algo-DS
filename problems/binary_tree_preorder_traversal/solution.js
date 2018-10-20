/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {
  var output = [];
  var stack = [];
  var node = root;
  while (node || stack.length > 0) {
    if (node === null) {
      node = stack.pop();
    }
    output.push(node.val);
    if (node.right !== null) {
      stack.push(node.right);
    } 
    node = node.left;
  }
  return output;
};