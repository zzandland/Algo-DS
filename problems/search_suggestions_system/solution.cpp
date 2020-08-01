struct Node {
    vector<string> words;
    unordered_map<char, Node*> next;
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        Node* trie = new Node();
        
        for (string prod: products) {
            Node* n = trie;
            for (char c: prod) {
                if (!n->next[c]) n->next[c] = new Node();
                n = n->next[c];
                n->words.push_back(prod);
            }
        }
        
        vector<vector<string>> res;
        Node* n = trie;
        for (char c: searchWord) {
            if (!n->next[c]) n->next[c] = new Node();
            n = n->next[c];
            vector<string> words = n->words;
            sort(words.begin(), words.end(), [](string a, string b) { return a.compare(b) < 0; });
            vector<string> slice = words.size() > 3 ? vector<string>(words.begin(), words.begin()+3) : words;
            res.push_back(slice);
        }
        
        return res;
    }
};