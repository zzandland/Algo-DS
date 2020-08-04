class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        
        # make prefix matrix
        p = [[0]*(n+1) for _ in range(m+1)]
        for y in range(m):
            for x in range(n):
                p[y+1][x+1] = matrix[y][x] + p[y+1][x] + p[y][x+1] - p[y][x]
                
        res = 0
        for y2 in range(1, m+1):
            for y1 in range(y2):
                run = 0
                seen = Counter({0: 1})
                for x in range(1, n+1):
                    tmp = p[y2][x] - p[y1][x]
                    res += seen[target-tmp]
                    seen[-tmp] += 1
        return res