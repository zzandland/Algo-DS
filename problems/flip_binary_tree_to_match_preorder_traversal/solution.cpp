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
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        vector<int> res;
        int i = 0;
        if (dfs(root, res, i, voyage)) return res;
        return { -1 };
    }
    
    bool dfs(TreeNode* root, vector<int>& res, int& i, vector<int>& voyage) {
        if (!root) return true;
        if (voyage[i] != root->val) return false;
        ++i;
        if (root->left && root->left->val != voyage[i]) {
            res.push_back(root->val);
            return dfs(root->right, res, i, voyage) && dfs(root->left, res, i, voyage);
        }
        return dfs(root->left, res, i, voyage) && dfs(root->right, res, i, voyage);
    }
};