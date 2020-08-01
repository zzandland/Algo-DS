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

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(Node* root) {
        ostringstream ss;
        serialize_helper(root, ss);
        return ss.str();
    }
    
    void serialize_helper(Node* root, ostringstream& ss) {
        if (!root) return;
        ss << " " << root->val << " " << root->children.size();
        for (Node* p: root->children) serialize_helper(p, ss);
    }
	
    // Decodes your encoded data to tree.
    Node* deserialize(string data) {
        istringstream ss(data);
        return deserialize_helper(ss);
    }
    
    Node* deserialize_helper(istringstream& ss) {
        ss.peek();
        if (ss.eof()) return nullptr; 
        Node* root = new Node();
        int size;
        ss >> root->val >> size;
        for (int i = 0; i < size; ++i) root->children.push_back(deserialize_helper(ss));
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));