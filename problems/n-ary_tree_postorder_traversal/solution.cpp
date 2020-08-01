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
    vector<int> postorder(Node* root) {
        vector<int> res;
        if (!root) return res;
        stack<Node*> st;
        st.push(root);
        while (!st.empty()) {
            Node* n = st.top();
            st.pop();
            res.push_back(n->val);
            stack<Node*> tmp;
            for (Node* child: n->children) st.push(child);
            while (!tmp.empty()) {
                st.push(tmp.top());
                tmp.pop();
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};