class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = y = x = 0
        dir_ = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = {(0, 0)}
        for i in range(4):
            for c in instructions:
                if c == 'L':
                    d = (d+3) % 4
                elif c == 'R':
                    d = (d+1) % 4
                else:
                    y += dir_[d][0]
                    x += dir_[d][1]
        return (x == 0 and y == 0) or d != 0