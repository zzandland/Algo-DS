/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {boolean}
 */
var hasPathSum = function(root, sum) {
    if (!root) {
        return false;
    }
    var sumArr = [];
    var innerFunc = function(node, val) {
        val += node.val;
        if (!node.left && !node.right) {
            sumArr.push(val);
        }
        if (node.left) {
            innerFunc(node.left, val);
        }
        if (node.right) {
            innerFunc(node.right, val);
        }
    }
    innerFunc(root, 0);
    return sumArr.includes(sum);
};