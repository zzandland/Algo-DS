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
    bool isValidBST(TreeNode* root) {
        long MAX = ~0UL >> 1;
        return helper(root, ~MAX, MAX);
    }
    
    bool helper(TreeNode *root, long l, long r) {
        if (!root) return true;
        return root->val > l && root->val < r && helper(root->left, l, root->val) && helper(root->right, root->val, r);
    }
};