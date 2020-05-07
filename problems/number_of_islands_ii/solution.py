class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if m == 0 or n == 0: return 0
        dp, cnt = [-1 for i in range(m*n)], 0
        
        def find(n: int) -> int:
            if dp[n] != n: dp[n] = find(dp[n])
            return dp[n]    
        
        def union(a: int, b: int) -> None:
            fa, fb = find(a), find(b)
            dp[fa] = b
                
        output = []        
        for y, x in positions:
            o = y*n+x
            if dp[o] == -1:
                cnt += 1
                dp[o] = o
                for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = y+r, x+c
                    no = ny*n+nx
                    if 0 <= ny < m and 0 <= nx < n and dp[no] != -1 and find(o) != find(no):
                        cnt -= 1
                        union(o, no)
            output.append(cnt)        
        return output    