class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        W, B = len(workers), len(bikes)
        def cal(w: int, b: int) -> int: 
            wy, wx = workers[w]
            by, bx = bikes[b]
            return abs(wy - by) + abs(wx - bx)
        
        dp = {}
        
        def dq(w: int, b: int) -> int:
            if w == W: return 0
            if b not in dp:
                res = float('inf')
                for i in range(B):
                    if b & (1 << i) == 0:
                        res = min(res, cal(w, i) + dq(w+1, b ^ (1 << i)))
                dp[b] = res
            return dp[b]
        
        return dq(0, 0)