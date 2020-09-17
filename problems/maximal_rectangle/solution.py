class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        N, M = len(matrix), len(matrix[0])
        
        dp = [[0]*M for _ in range(N)]
        for y in range(N):
            for x in range(M):
                if matrix[y][x] == '1': dp[y][x] = 1 + dp[y-1][x]
                    
        def minHistogram(row: [int]) -> int:
            st = []
            left = [-1]*M
            right = [M]*M
            for i, h in enumerate(row):
                while st and st[-1][0] > h:
                    right[st.pop()[1]] = i
                if st: left[i] = st[-1][1]
                st.append((h, i))
            return max([row[i] * (right[i] - left[i] - 1) for i in range(M)])
        
        return max([minHistogram(row) for row in dp])
            