class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        M, N = len(matrix), len(matrix[0])
        h, l, r = [0]*N, [0]*N, [N-1]*N
        res = 0
        
        # for each row O(m)
        # O(3mn)
        for y in range(M):
            
            # calculate maximum height from the cell O(n)
            for x in range(N):
                if matrix[y][x] == '1': h[x] += 1
                else: h[x] = 0
                    
            # calculate left index limit that makes a rectangle O(n)
            cur_left_bound = 0
            for x in range(N):
                if matrix[y][x] == '1':
                    l[x] = max(l[x], cur_left_bound)
                else:
                    l[x] = 0
                    cur_left_bound = x + 1
                    
            # calculate right index limit that makes a rectangle O(n)
            cur_right_bound = N-1
            for x in range(N-1, -1, -1):
                if matrix[y][x] == '1':
                    r[x] = min(r[x], cur_right_bound)
                else:
                    r[x] = N-1
                    cur_right_bound = x - 1
                    
            # calculate maximum area from the cell O(n)
            for x in range(N):
                res = max(res, (r[x] - l[x] + 1) * h[x])
                
        return res