class Solution {
public:
    vector<vector<char>> board_;
    vector<int> dir_{-1, 0, 1, 0, -1};
    string word_;
    int Y_, X_;
    
    bool exist(vector<vector<char>>& board, string word) {
        board_ = board;
        word_= word;
        Y_ = board.size();
        X_ = board[0].size();
        vector<vector<bool>> seen(Y_, vector<bool>(X_, false));
        for (int y = 0; y < Y_; ++y) {
            for (int x = 0; x < X_; ++x) {
                if (dfs(y, x, 0, seen)) return true;
            }
        }
        return false;
    }
    
    bool dfs(int y, int x, int i, vector<vector<bool>> &seen) {
        if (seen[y][x] || word_[i] != board_[y][x]) return false;
        if (i == word_.length() - 1) return true;
        seen[y][x] = true;
        for (int j = 0; j < 4; ++j) {
            int ny = dir_[j] + y, nx = dir_[j+1] + x;
            if (0 <= ny && ny < Y_ && 0 <= nx && nx < X_) {
                if (dfs(ny, nx, i+1, seen)) return true;
            }
        }
        seen[y][x] = false;
        return false;
    }
};