class Solution {
public:
    int movesToChessboard(vector<vector<int>>& board) {
        size_t N = board.size(), rowSum = 0, colSum = 0, rowSwap = 0, colSwap = 0;
        
        // check if all corners are all 0s or 1s
        for (size_t y = 0; y < N; ++y) {
            for (size_t x = 0; x < N; ++x) {
                if ((board[0][0] ^ board[y][0] ^ board[0][x] ^ board[y][x]) != 0) {
                    return -1;
                }
            }
        }
        
        for (size_t i = 0; i < N; ++i) {
            rowSum += board[0][i];
            colSum += board[i][0];
            if (board[0][i] == i % 2) {
                ++rowSwap;
            } 
            if (board[i][0] == i % 2) {
                ++colSwap;
            }
        }
        
        if (rowSum != N / 2 && rowSum != (N + 1) / 2) {
            return -1;
        }
        if (colSum != N / 2 && colSum != (N + 1) / 2) {
            return -1;
        }
        if (N % 2 == 1) {
            if (rowSwap % 2 == 1) {
                rowSwap = N - rowSwap;
            }
            if (colSwap % 2 == 1) {
                colSwap = N - colSwap;
            }
        } else {
            rowSwap = min(rowSwap, N - rowSwap);
            colSwap = min(colSwap, N - colSwap);
        }
        return (rowSwap + colSwap) / 2;
    }
};