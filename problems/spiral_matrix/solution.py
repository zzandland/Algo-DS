class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        output = []
        w, h = len(matrix[0]), len(matrix)
        i = 0
        while w > 0 and h > 0:
            if w > 1 and h > 1:
                self.rotate(i, matrix, output)
            elif w > 1:
                self. hor(i, matrix, output)    
            elif h > 1:
                self.ver(i, matrix, output)    
            else:
                output.append(matrix[i][i])    
            i += 1    
            w -= 2
            h -= 2
        return output    
    
    def rotate(self, i: int, matrix: List[List[int]], output: List[int]) -> None:
        y = x = i
        while x < len(matrix[0]) - i - 1:
            output.append(matrix[y][x])
            x += 1
        while y < len(matrix) - i - 1:
            output.append(matrix[y][x])
            y += 1
        while x > i:
            output.append(matrix[y][x])
            x -= 1
        while y > i:    
            output.append(matrix[y][x])
            y -= 1
            
    def hor(self, i: int, matrix: List[List[int]], output: List[int]) -> None:
        for col in range(i, len(matrix[0]) - i):
            output.append(matrix[i][col])
            
    def ver(self, i: int, matrix: List[List[int]], output: List[int]) -> None:
        for row in range(i, len(matrix) - i):
            output.append(matrix[row][i])