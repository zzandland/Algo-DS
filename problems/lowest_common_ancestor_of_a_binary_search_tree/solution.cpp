/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode *p, *q, *res;

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        this->p = p;
        this->q = q;
        dfs(root);
        return res;
    }
    
    bool dfs(TreeNode* node) {
        if (!node || res) return false;
        bool l = dfs(node->left), r = dfs(node->right);
        if (l && r) {
            res = node;
            return true;
        }
        if (node == this->p || node == this->q) {
            if (l || r) res = node;
            return true;
        }
        return l || r;
    }
};