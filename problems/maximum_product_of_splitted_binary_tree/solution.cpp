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
    long total = 0, res = 0;
    int maxProduct(TreeNode* root) {
        total = dfs(root), dfs(root);
        return res % (int)(1e9 + 7);
    }
    
    int dfs(TreeNode* root) {
        if (root == nullptr) return 0;
        int sum = dfs(root->left) + dfs(root->right) + root->val;
        res = max(res, (total - sum) * sum);
        return sum;
    }
};