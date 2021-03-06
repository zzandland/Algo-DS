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
    if (!root) {
        return [];
    }
    var output = [];
    var innerFunc = function(node) {
        if (node.left) {
            innerFunc(node.left);
        }
        if (node.right) {
            innerFunc(node.right);
        }
        output.push(node.val);  
    }
    innerFunc(root);
    return output;  
};