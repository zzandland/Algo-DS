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
var maxDepth = function(root) {
    if (!root) {
        return 0;
    }
    var output = 0;
    var innerFunc = function(node, depth) {
        output = Math.max(depth, output);
        if (node.left) {
            innerFunc(node.left, depth + 1);
        }
        if (node.right) {
            innerFunc(node.right, depth + 1);
        }
    }
    innerFunc(root, 1);
    return output;
};