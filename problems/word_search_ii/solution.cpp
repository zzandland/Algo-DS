class Solution {
    struct Node {
        Node* next[26];
        int idx = -1;

        Node() {
            fill_n(next, 26, nullptr);
        }
        
        ~Node() {
            for (int i = 0; i < 26; ++i) delete next[i];
        }
    };

public:
    Node *root_;
    int Y, X;
    
    void makeTrie(const vector<string>& words) {
        root_ = new Node();
        Node *n;
        for (int i = 0; i < words.size(); ++i) {
            n = root_;
            for (const char c : words[i]) {
                int idx = c - 'a';
                if (!n->next[idx]) n->next[idx] = new Node();
                n = n->next[idx];
            }
            n->idx = i;
        }
    }
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        makeTrie(words);
        vector<string> res;
        Y = board.size(), X = board[0].size();
        int Z = words.size();
        if (Y == 0 || X == 0 || Z == 0) return res;
        
        for (int y = 0; y < Y; ++y) {
            for (int x = 0; x < X && Z > res.size(); ++x) {
                dfs(board, root_, res, words, y, x);
            }
        }
        delete root_;
        return res;
    }
    
    void dfs(vector<vector<char>>& board, Node *n, vector<string> &res, const vector<string> &words, int y, int x) {
        char tmp = board[y][x];
        if (board[y][x] == 'X' || n->next[tmp - 'a'] == nullptr) return;
        Node *nxt = n->next[tmp - 'a'];
        if (nxt->idx != -1) {
            res.push_back(words[nxt->idx]);
            nxt->idx = -1;
        }
        board[y][x] = 'X';
        vector<int> dir{-1, 0, 1, 0, -1};
        if (y > 0) dfs(board, nxt, res, words, y - 1, x);
        if (y < Y-1) dfs(board, nxt, res, words, y + 1, x);
        if (x > 0) dfs(board, nxt, res, words, y, x - 1);
        if (x < X-1) dfs(board, nxt, res, words, y, x + 1);
        board[y][x] = tmp;
    }
};