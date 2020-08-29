# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def rotate(d: int, t: int) -> int:
            while d != t:
                robot.turnRight()
                d = (d+1) % 4
            return t

        dir_ = ((-1, 0), (0, 1), (1, 0), (0, -1))
        def dfs(y: int, x: int, d: int, seen: set) -> int:
            if (y, x) in seen:
                d = rotate(d, (d+2) % 4)
                robot.move()
                return d
            robot.clean()
            seen.add((y, x))
            a = d
            for i in range(4):
                a = rotate(a, i)
                if not robot.move(): continue
                ny, nx = y + dir_[i][0], x + dir_[i][1]
                a = dfs(ny, nx, a, seen)
                
            a = rotate(a, (d+2) % 4)
            robot.move()
            return a
        
        dfs(0, 0, 0, set())