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
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q;
        q.emplace(root);
        int res = 0;
        while (!q.empty()) {
            res++;
            int len = q.size();
            for (int i = 0; i < len; ++i) {
                TreeNode *n = q.front();
                q.pop();
                if (!n->left && !n->right) return res;
                if (n->left) q.emplace(n->left);
                if (n->right) q.emplace(n->right);
            }
        }
        return res;
    }
};