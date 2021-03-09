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
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if (d == 1) {
            TreeNode *res = new TreeNode(v);
            res->left = root;
            return res;
        }
        dfs(root, v, d, 1);
        return root;
    }
    
    void dfs(TreeNode *root, int v, int d, int c) {
        if (!root) return;
        if (d-1 == c) {
            TreeNode *l = new TreeNode(v);
            if (root->left) l->left = root->left;
            root->left = l;
            
            TreeNode *r = new TreeNode(v);
            if (root->right) r->right = root->right;
            root->right = r;
            return;
        }
        dfs(root->left, v, d, c+1);
        dfs(root->right, v, d, c+1);
    }
};