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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        if (root) {
            vector<int> tmp;
            dfs(root, sum, 0, tmp, res);
        }
        return res;
    }
    
    void dfs(TreeNode* root, int sum, int run, vector<int>& tmp, vector<vector<int>>& res) {
        run += root->val;
        if (!root->left && !root->right) {
            if (run == sum) {
                vector<int> out = tmp;
                out.push_back(root->val);
                res.push_back(out);
            }
            return;
        }
        
        tmp.push_back(root->val);
        if (root->left) dfs(root->left, sum, run, tmp, res);
        if (root->right) dfs(root->right, sum, run, tmp, res);
        tmp.pop_back();
        return;
    }
};