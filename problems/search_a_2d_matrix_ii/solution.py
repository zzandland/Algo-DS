class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r, c = len(matrix)-1, 0
        while 0 <= r and c < len(matrix[0]):
            cell = matrix[r][c]
            if cell == target: return True
            elif cell > target: r-=1
            else: c+=1    
        return False    