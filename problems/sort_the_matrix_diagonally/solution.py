class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat: return []
        m, n = len(mat), len(mat[0])
        arr = [(r, 0) for r in range(m-1, 0, -1)] + [(0, c) for c in range(n)]
        for r, c in arr:
            tmp = []
            y, x = r, c
            while y < m and x < n:
                tmp.append(mat[y][x])
                y += 1
                x += 1
            tmp.sort()
            y, x = r, c
            for val in tmp:
                mat[y][x] = val
                y += 1
                x += 1
        return mat