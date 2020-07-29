class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 N 1 E 2 S 3 W
        # if dir pointing is clock/counterclockwise or N/S circle
        if 'G' not in instructions: return True
        new_coord, new_d = self.run(instructions, [0, 0], 0)
        if new_d == 0:
            y, x = new_coord
            if x == 0 and y == 0: return True
            return False
        return new_d in (1, 2, 3)
        
    def run(self, instructions: str, coord: List[int], d: int) -> List[int]:
        dir_ = ((-1, 0), (0, 1), (1, 0), (0, -1))
        for c in instructions:
            if c == 'L':
                d -= 1
                if d == -1: d = 3
            elif c == 'R':
                d += 1
                if d == 4: d = 0
            else:
                r, c = dir_[d]
                coord[0] += r
                coord[1] += c
        return [coord, d]