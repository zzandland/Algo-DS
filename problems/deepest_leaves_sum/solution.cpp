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
    int deepestLeavesSum(TreeNode* root) {
        dfs(root, 0);
        return sum;
    }
    
    void dfs(TreeNode* root, int level) {
        if (!root) return;
        if (level > deepest) {
            deepest = level;
            sum = 0;
        }
        if (level == deepest)  sum += root->val;
        dfs(root->left, level + 1), dfs(root->right, level + 1);
    }
    
private:
    int sum = 0;    
    int deepest = -1;
};