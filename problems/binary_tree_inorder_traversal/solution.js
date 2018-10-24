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
var inorderTraversal = function(root) {
    if (!root) {
        return [];
    }
    var output = [];
    var innerFunc = function(node) {
        if (node.left) {
            innerFunc(node.left);
        }
        output.push(node.val);  
        if (node.right) {
            innerFunc(node.right);
        }
    }
    innerFunc(root);
    return output;
};