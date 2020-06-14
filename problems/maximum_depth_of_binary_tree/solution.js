/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    var dfs = function(n, depth) {
        if (!n) return 0;
        return Math.max(depth, Math.max(dfs(n.left, depth+1), dfs(n.right, depth+1)))
    }
    return dfs(root, 1)
};