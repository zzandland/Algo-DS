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
    if (!root) {
        return [];
    }
    var output = [];
    var innerFunc = function(node) {
        output.push(node.val);  
        if (node.left) {
            innerFunc(node.left);
        }
        if (node.right) {
            innerFunc(node.right);
        }
    }
    innerFunc(root);
    return output;
};