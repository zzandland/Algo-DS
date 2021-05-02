struct TrieNode {
    unordered_set<string> matches;
    vector<TrieNode*> next;
    
    TrieNode(): next(26, nullptr) {}
};

class WordFilter {
public:
    WordFilter(vector<string>& words) {
        prefix = new TrieNode();
        suffix = new TrieNode();
        idx[""] = -1;
        for (int i = 0; i < words.size(); ++i) {
            string w = words[i];
            idx[w] = i;
            TrieNode * tmp = prefix;
            for (char c : w) {
                int idx = c - 'a';
                if (!tmp->next[idx]) tmp->next[idx] = new TrieNode();
                tmp = tmp->next[idx];
                tmp->matches.insert(w);
            }
            tmp = suffix;
            for (int j = w.length() - 1; j >= 0; --j) {
                int idx = w[j] - 'a';
                if (!tmp->next[idx]) tmp->next[idx] = new TrieNode();
                tmp = tmp->next[idx];
                tmp->matches.insert(w);
            }
        }
    }
    
    int f(string prefix, string suffix) {
        TrieNode *tmp = this->prefix;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!tmp->next[idx]) return -1;
            tmp = tmp->next[idx];
        }
        unordered_set<string> preset = tmp->matches;
        tmp = this->suffix;
        for (int i = suffix.length() - 1; i >= 0; --i) {
            int idx = suffix[i] - 'a';
            if (!tmp->next[idx]) return -1;
            tmp = tmp->next[idx];
        }
        unordered_set<string> sufset = tmp->matches;
        string res = "";
        for (const auto &p : preset)
            if (sufset.count(p)) {
                if (p.length() > res.length() ||
                    (p.length() == res.length() && idx[p] > idx[res])
                   ) res = p;
            }
        return idx[res];
    }
    
private:
    TrieNode *prefix, *suffix;
    unordered_map<string, int> idx;
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(prefix,suffix);
 */