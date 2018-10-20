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
var postorderTraversal = function(root) {
  var output = [];
  var innerFunc = function(node) {
    if (node !== null) {
      innerFunc(node.left);
      innerFunc(node.right);
      output.push(node.val);
    }
  }
  innerFunc(root);
  
  return output;
};