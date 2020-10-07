/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* initTreeNode(int val) {
    struct TreeNode* output = malloc(sizeof(struct TreeNode));
    output->val = val;
    output->left = output->right = NULL;
    return output;
}

struct TreeNode* insertIntoBST(struct TreeNode* root, int val){
    if (!root) return initTreeNode(val);
    if (root->val < val) root->right = insertIntoBST(root->right, val);
    else root->left = insertIntoBST(root->left, val);
    return root;
}