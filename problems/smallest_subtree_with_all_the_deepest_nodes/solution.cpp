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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        return dfs(root).first;
    }
    
    pair<TreeNode*, int> dfs(TreeNode *root) {
        if (!root) return make_pair(root, 0);
        pair<TreeNode*, int> l = dfs(root->left), r = dfs(root->right);
        if (l.second > r.second) return make_pair(l.first, l.second+1);
        if (l.second < r.second) return make_pair(r.first, r.second+1);
        return make_pair(root, l.second+1);
    }
};