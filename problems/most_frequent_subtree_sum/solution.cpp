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
    vector<int> findFrequentTreeSum(TreeNode* root) {
        if (!root) return vector<int>();
        unordered_map<int, int> freq;
        dfs(root, freq);
        vector<pair<int, int>> pairs;
        for (const auto &[key, val] : freq) pairs.push_back({key, val});
        auto cmp = [&](pair<int, int> &a, pair<int, int> &b) -> bool {
            return a.second < b.second;
        };
        make_heap(pairs.begin(), pairs.end(), cmp);
        vector<int> res;
        int t, f;
        t = f = pairs.front().second;
        do {
            auto p = pairs.front();
            f = p.second;
            res.push_back(p.first);
            pop_heap(pairs.begin(), pairs.end(), cmp);
            pairs.pop_back();
            t = pairs.front().second;
        } while (f == t && !pairs.empty());
        return res;
    }
    
    int dfs(TreeNode *root, unordered_map<int, int> &freq) {
        if (!root) return 0;
        int sum = root->val + dfs(root->left, freq) + dfs(root->right, freq);
        freq[sum]++;
        return sum;
    }
};