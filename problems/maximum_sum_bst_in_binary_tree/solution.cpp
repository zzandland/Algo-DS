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
#define EMPTY tuple<int, int, int> {INT_MAX, INT_MAX, INT_MAX}
#define FAIL tuple<int, int, int> {INT_MIN, INT_MIN, INT_MIN}
typedef tuple<int, int, int> e;

class Solution {
public:
    int maxSumBST(TreeNode* root) {
        int mx = 0;
        helper(root, mx);
        return mx;
    }
    
    e helper(TreeNode* root, int& mx) {
        if (!root) return EMPTY;
        e left = helper(root->left, mx), right = helper(root->right, mx);
        if (left == FAIL || right == FAIL) return FAIL;
        int sm, l, r;
        sm = l = r = root->val;
        
        if (left != EMPTY) {
            if (get<1>(left) >= root->val) return FAIL;
            sm += get<2>(left);
            l = get<0>(left);
        }
        
        if (right != EMPTY) {
            if (get<0>(right) <= root->val) return FAIL;
            sm += get<2>(right);
            r = get<1>(right);
        }
        
        mx = max(mx, sm);
        return make_tuple(l, r, sm);
    }
};