class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir_ = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        y = x = 0
        for m in moves:
            y += dir_[m][0]
            x += dir_[m][1]
        return y == x == 0