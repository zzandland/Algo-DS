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
    int pathSum(TreeNode* root, int sum) {
        unordered_map<int, int> seen;
        seen[0] = 1;
        return dfs(root, 0, sum, seen);
    }
    
    int dfs(TreeNode* root, int run, int sum, unordered_map<int, int>& seen) {
        if (!root) return 0;
        run += root->val;
        int res = seen[run - sum];
        ++seen[run];
        res += dfs(root->left, run, sum, seen) + dfs(root->right, run, sum, seen);
        --seen[run];
        return res;
    }
};