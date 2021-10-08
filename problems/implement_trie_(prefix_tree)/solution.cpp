struct Node {
    bool term = false;
    vector<Node*> nxt;
    
    Node(): nxt(27, nullptr) {}
};

class Trie {
public:
    Node *root_ = nullptr;
    
    Trie() {
        root_ = new Node();
    }
    
    void insert(string word) {
        Node *n = root_;
        for (const char c : word) {
            int i = c - 'a';
            if (!n->nxt[i]) {
                n->nxt[i] = new Node();
            }
            n = n->nxt[i];
        }
        n->term = true;
    }
    
    bool search(string word) {
        Node *n = root_;
        for (const char c : word) {
            int i = c -'a';
            if (!n->nxt[i]) return false;
            n = n->nxt[i];
        }
        return n->term;
    }
    
    bool startsWith(string prefix) {
        Node *n = root_;
        for (const char c : prefix) {
            int i = c -'a';
            if (!n->nxt[i]) return false;
            n = n->nxt[i];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */