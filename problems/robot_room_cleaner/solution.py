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
        dir_, visited, opp = ['u', 'r', 'd', 'l'], set([(0, 0)]), {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}
        dirDic = {'u': (1, 0), 'd': (-1, 0), 'l': (0, -1), 'r': (0, 1)}
        sy = sx = d = 0
        def rotate(t: str) -> None:
            nonlocal d
            while dir_[d] != t:
                robot.turnRight()
                d = (d+1) % 4
        def dfs(y: int, x: int, prev: str) -> None:
            robot.clean()
            for dd in dir_:
                if dd == opp[dd]: continue
                rotate(dd)
                r, c = dirDic[dd]
                ny, nx = y+r, x+c
                if (ny, nx) not in visited and robot.move():
                    visited.add((ny, nx))
                    dfs(y+r, x+c, dd)
            rotate(opp[prev])
            robot.move()    
        dfs(0, 0, 'u')    