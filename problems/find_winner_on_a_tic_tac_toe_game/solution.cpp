class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        vector<int> rows(3, 0), cols(3, 0);
        int diag = 0, aDiag = 0, player = 1;
        for (auto m : moves) {
            int y = m[0], x = m[1];
            rows[y] += player;
            cols[x] += player;
            if (y == x) diag += player;
            if (y + x == 2) aDiag += player;
            if (abs(rows[y]) == 3 || abs(cols[x]) == 3 || abs(diag) == 3 || abs(aDiag) == 3)
                return player == 1 ? "A" : "B";
            player *= -1;
        }
        return moves.size() == 9 ? "Draw" : "Pending";
    }
};