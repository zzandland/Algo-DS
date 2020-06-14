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
 * @return {boolean}
 */
var isUnivalTree = function(root) {
    if (!root) return false;
    st = [root]
    while (st.length) {
        n = st.pop();
        if (n.val != root.val) return false;
        if (n.left) st.push(n.left);
        if (n.right) st.push(n.right);
    }
    return true;
};