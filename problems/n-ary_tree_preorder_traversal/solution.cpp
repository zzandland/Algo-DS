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

class Solution {
public:
    vector<int> preorder(Node* root) {
        if (!root) return vector<int>();
        stack<Node*> st;
        st.push(root);
        vector<int> res;
        while (!st.empty()) {
            Node* n = st.top();
            st.pop();
            res.push_back(n->val);
            stack<Node*> tmp;
            for (Node* p: n->children) tmp.push(p);
            while (!tmp.empty()) {
                st.push(tmp.top());
                tmp.pop();
            }
        }
        return res;
    }
};