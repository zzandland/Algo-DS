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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<long> depths;
        vector<int> cnts;
        dfs(root, 0, depths, cnts);
        vector<double> res;
        for (int i = 0; i < depths.size(); ++i) res.push_back(depths[i] / (double)cnts[i]);
        return res;
    }
    
    void dfs(TreeNode *root, int depth, vector<long> &depths, vector<int> &cnts) {
        if (!root) return;
        if (depth >= depths.size()) {
            depths.push_back(0);
            cnts.push_back(0);
        }
        depths[depth] += root->val;
        cnts[depth]++;
        dfs(root->left, depth + 1, depths, cnts);
        dfs(root->right, depth + 1, depths, cnts);
    }
};