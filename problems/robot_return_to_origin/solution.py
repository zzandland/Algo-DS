class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        y = x = 0
        for c in moves:
            r, c = dic[c]
            y += r
            x += c
        return (y, x) == (0, 0)