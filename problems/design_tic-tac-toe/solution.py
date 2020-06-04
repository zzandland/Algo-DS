class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.b = [[None]*n for _ in range(n)]
        
    def _hor(self, row: int, col: int, p: int) -> bool:
        return all([col == p for col in self.b[row]])
    
    def _ver(self, row: int, col: int, p: int) -> bool:
        return all([row[col] == p for row in self.b])
    
    def _diag(self, row: int, col: int, p: int) -> bool:
        N = len(self.b)
        if row == col or row + col == N-1:
            return (
                all([self.b[i][i] == p for i in range(N)]) or
                all([self.b[N-i-1][i] == p for i in range(N)])
            )
        return False
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.b[row][col] = player
        if any([check(row, col, player) for check in (self._hor, self._ver, self._diag)]):
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)