/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) return 0;
        int res = 0;
        dfs(root, res);
        return res;
    }
    
    int dfs(TreeNode *node, int &root) {
        if (!node) return 0;
        int l = dfs(node->left, root), r = dfs(node->right, root);
        root = max(root, l + r);
        return 1 + max(l, r);
    }
};