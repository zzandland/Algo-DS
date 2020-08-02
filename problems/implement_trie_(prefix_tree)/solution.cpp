struct Node {
    bool end;
    unordered_map<char, Node*> next;
    Node(): end(false) {}
};

class Trie {
public:
    Node* root;
    
    /** Initialize your data structure here. */
    Trie(): root(new Node()) {}
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Node* n = root;
        for (char c: word) {
            if (!n->next.count(c)) n->next[c] = new Node();
            n = n->next[c];
        }
        n->end = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Node* n = root;
        for (char c: word) {
            if (!n->next.count(c)) return false;
            n = n->next[c];
        }
        return n->end;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Node* n = root;
        for (char c: prefix) {
            if (!n->next.count(c)) return false;
            n = n->next[c];
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