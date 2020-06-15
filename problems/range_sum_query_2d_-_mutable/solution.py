class Node:
    def __init__(self, val: int, y1: int, y2: int, x1: int, x2: int):
        self.val = val
        self.y1, self.y2 = y1, y2
        self.x1, self.x2 = x1, x2
        self.left = self.right = None

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.R, self.C = len(matrix), len(matrix[0])
        tmp = [[0]*(self.C+1) for _ in range(self.R+1)]
        for y in range(1, self.R+1):
            for x in range(1, self.C+1):
                tmp[y][x] = (matrix[y-1][x-1] + tmp[y-1][x] +
                             tmp[y][x-1] - tmp[y-1][x-1])
        def fn(y1: int, y2: int, x1: int, x2: int) -> Node:
            val = tmp[y2+1][x2+1] - tmp[y2+1][x1] - tmp[y1][x2+1] + tmp[y1][x1]
            n = Node(val, y1, y2, x1, x2)
            if y1 == y2 and x1 == x2:
                return n
            if y1 < y2:
                m = y1 + (y2-y1)//2
                n.left = fn(y1, m, x1, x2)
                n.right = fn(m+1, y2, x1, x2)
            else:
                m = x1 + (x2-x1)//2
                n.left = fn(y1, y2, x1, m)
                n.right = fn(y1, y2, m+1, x2)
            return n
        self.root = fn(0, self.R-1, 0, self.C-1)

    def update(self, row: int, col: int, val: int) -> None:
        def fn(n: Node) -> int:
            if n.y1 == n.y2 == row and n.x1 == n.x2 == col:
                diff = n.val - val
                n.val = val
                return diff
            if n.y1 < n.y2:
                m = n.y1 + (n.y2-n.y1)//2
                diff = fn(n.left) if row <= m else fn(n.right)
            else:
                m = n.x1 + (n.x2-n.x1)//2
                diff = fn(n.left) if col <= m else fn(n.right)
            n.val -= diff
            return diff
        fn(self.root)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def fn(n: Node, y1: int, y2: int, x1: int, x2: int) -> int:
            if n.y1 == y1 and n.y2 == y2 and n.x1 == x1 and n.x2 == x2:
                return n.val
            if n.y1 < n.y2:
                m = n.y1 + (n.y2-n.y1)//2
                if y2 <= m:
                    return fn(n.left, y1, y2, x1, x2)
                elif y1 > m:
                    return fn(n.right, y1, y2, x1, x2)
                return fn(n.left, y1, m, x1, x2) + fn(n.right, m+1, y2, x1, x2)
            else:
                m = n.x1 + (n.x2-n.x1)//2
                if x2 <= m:
                    return fn(n.left, y1, y2, x1, x2)
                elif x1 > m:
                    return fn(n.right, y1, y2, x1, x2)
                return fn(n.left, y1, y2, x1, m) + fn(n.right, y1, y2, m+1, x2)
        return fn(self.root, row1, row2, col1, col2)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)