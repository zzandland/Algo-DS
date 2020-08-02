/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Codec {
public:
    // Encodes an n-ary tree to a binary tree.
    TreeNode* encode(Node* root) {
        if (!root) return nullptr;
        TreeNode* bin_root = new TreeNode(root->val);
        TreeNode* first = nullptr;
        TreeNode* run = nullptr;
        for (auto child: root->children) {
            TreeNode* tmp = encode(child);
            if (run != NULL) run->right = tmp;
            run = tmp;
            if (!first) first = run;
        }
        bin_root->left = first;
        return bin_root;
    }
	
    // Decodes your binary tree to an n-ary tree.
    Node* decode(TreeNode* root) {
        if (!root) return NULL;
        vector<Node*> children;
        TreeNode* child;
        if ((child = root->left) != NULL) {
            while (child != NULL) {
                Node* tmp = decode(child);
                children.push_back(tmp);
                child = child->right;
            }
        }
        return new Node(root->val, children);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(root));