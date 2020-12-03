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
    TreeNode *cur; 
    
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode *dummy = new TreeNode();
        this->cur = dummy;
        inorder(root);
        return dummy->right;
    }
    
    void inorder(TreeNode *root) {
        if (!root) return;
        inorder(root->left);
        root->left = nullptr;
        this->cur->right = root;
        this->cur = root;
        inorder(root->right);
    }
};