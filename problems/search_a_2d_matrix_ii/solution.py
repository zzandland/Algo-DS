class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        y, x = len(matrix)-1, 0
        while y >= 0 and x < len(matrix[0]):
            if target == matrix[y][x]: return True
            if target < matrix[y][x]: y -= 1
            else: x += 1
        return False