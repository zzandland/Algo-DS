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
    int goodNodes(TreeNode* root) {
        return dfs(root, INT_MIN);
    }
    
    int dfs(TreeNode* root, int mx) {
        if (!root) return 0;
        int new_mx = max(mx, root->val);
        int res = new_mx == root->val;
        return res + dfs(root->left, new_mx) + dfs(root->right, new_mx);
    }
};