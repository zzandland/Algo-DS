struct Node {
    bool end;
    Node* next[26];
    Node(): end(false) { fill_n(next, 26, nullptr); }
};

class WordDictionary {
public:
    Node* root;

    /** Initialize your data structure here. */
    WordDictionary(): root(new Node()) {}
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        Node* n = root;
        for (char c: word) {
            int idx = int(c) - 97;
            if (!n->next[idx]) n->next[idx] = new Node();
            n = n->next[idx];
        }
        n->end = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return dfs(word.c_str(), root);
    }
    
    bool dfs(const char* word, Node* root) {
        for (int i = 0; word[i] && root; ++i) {
            if (word[i] == '.') {
                for (Node* child: root->next) {
                    if (child && dfs(word+i+1, child)) return true;
                }
                return false;
            }
            root = root->next[int(word[i]) - 97];
        }
        return root && root->end;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */