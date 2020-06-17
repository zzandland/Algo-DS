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
        d = 0
        seen = set()
        dic = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        def turn(t: int):
            nonlocal d
            if d - t == 1 or d == 0 and t == 3:
                robot.turnLeft()
            elif d - t == -1 or d == 3 and t == 0:
                robot.turnRight()
            elif abs(d - t) == 2:
                robot.turnRight()
                robot.turnRight()
            d = t
        def dfs(y: int, x: int, p: int):
            robot.clean()
            for dd in dic:
                turn(dd)
                ny, nx = y+dic[dd][0], x+dic[dd][1]
                if (ny, nx) not in seen and robot.move():
                    seen.add((ny, nx))
                    dfs(y+dic[dd][0], x+dic[dd][1], dd)
            turn((p+2) % 4)
            robot.move()
        seen.add((0, 0))
        dfs(0, 0, 0)