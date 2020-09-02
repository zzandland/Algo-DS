class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        
        mn = float('inf')
        run = 0
        left = [0]*N
        for i, p in enumerate(prices):
            mn = min(mn, p)
            run = max(run, p - mn)
            left[i] = run
            
        mx = run = 0    
        right = [0]*N
        for i in range(N-1, -1, -1):
            mx = max(mx, prices[i])
            run = max(run, mx - prices[i])
            right[i] = run
            
        return max(a + b for a, b in zip(left, right))