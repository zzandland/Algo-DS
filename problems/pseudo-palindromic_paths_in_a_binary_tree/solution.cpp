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
    int pseudoPalindromicPaths (TreeNode* root) {
        int nums[10] = {0};
        return dfs(root, nums);
    }
    
    int dfs(TreeNode *root, int (&nums)[10]) {
        nums[root->val]++;
        int output = 0;
        if (!root->left && !root->right) {
            output += check(nums);
            nums[root->val]--;
            return output;
        }
        if (root->left) output += dfs(root->left, nums);
        if (root->right) output += dfs(root->right, nums);
        nums[root->val]--;
        return output;
    }
    
    bool check(int (&nums)[10]) {
        bool odd = false;
        for (int i = 1; i < 10; ++i) {
            if (nums[i] & 1 == 1) {
                if (odd) return false;
                odd = true;
            }
        }
        return true;
    }
};