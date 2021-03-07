struct Trie {
    vector<Trie*> children;
    
    Trie() : children(27, nullptr) {}
};

class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        Trie *root = new Trie();
        for (string w : words) {
            Trie *n = root;
            for (int i = w.length() - 1; i >= 0; --i) {
                int idx = w[i] - 'a';
                if (!n->children[idx]) n->children[idx] = new Trie();
                n = n->children[idx];
            }
        }
        return dfs(root, 0);
    }
    
    int dfs(Trie *root, int ln) {
        bool seen = false;
        int res = 0;
        for (int i = 0; i < 27; ++i) {
            if (root->children[i]) {
                seen = true;
                res += dfs(root->children[i], ln+1);
            }
        }
        return seen ? res : ln + 1;
    }
};