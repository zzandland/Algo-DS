#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (43.63%)
# Likes:    1483
# Dislikes: 65
# Total Accepted:    181.3K
# Total Submissions: 412.5K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# Example:
#
#
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
#
#
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        rows, cols, diags = set(), set(), set()
        output = []
        mtrx = [['.' for i in range(0, n)] for j in range(0, n)]
        def fn(r, c, cnt):
            if cnt >= n: output.append([row[:] for row in mtrx])
            if r == n:
                r += 1
                c = 0
            for y in range(c, n):
                start_x = c if y == c else 0
                for x in range(start_x, n):
                    if y not in rows and x not in rows and y-x not in diags and x-y not in diags:
                        rows.add(y)
                        cols.add(x)
                        diags.add(y-x)
                        mtrx[y][x] = 'Q'
                        fn(r, c+1, cnt+1)
                        rows.remove(y)
                        cols.remove(x)
                        diags.remove(abs(y))

# @lc code=end
