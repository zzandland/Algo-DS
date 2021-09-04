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
    int N;
    vector<TreeNode*> generateTrees(int n) {
        N = n;
        return dfs(1, n);
    }
    
    vector<TreeNode*> dfs(int l, int r) {
        vector<TreeNode*> res;
        if (l > r) {
            res.push_back(nullptr);
            return res;
        }
        for (int i = l; i <= r; ++i) {
            vector<TreeNode*> L = dfs(l, i-1), R = dfs(i+1, r);
            for (TreeNode* ll : L) {
                for (TreeNode* rr : R) {
                    TreeNode* n = new TreeNode(i, ll, rr);
                    res.push_back(n);
                }
            }
        }
        return res;
    }
};