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
    int sum = 0;
    
    TreeNode* sufficientSubset(TreeNode* root, int limit) {
        if (!root->left && !root->right) return sum + root->val < limit ? nullptr : root;
        sum += root->val;
        if (root->left) root->left = sufficientSubset(root->left, limit);
        if (root->right) root->right = sufficientSubset(root->right, limit);
        sum -= root->val;
        if (!root->left && !root->right) return nullptr;
        return root;
    }
};