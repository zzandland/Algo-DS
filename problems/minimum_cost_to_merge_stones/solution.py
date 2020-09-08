class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        prefix = [0]
        for n in stones:
            prefix.append(n + prefix[-1])
        
        dp = {}
        def dfs(l: int, r: int, k: int) -> int:
            if l == r and k == 1: return 0
            if (r - l + 1 - k) % (K - 1) != 0: return float('inf')
            if k == 1: return prefix[r+1] - prefix[l] + dfs(l, r, K)
            if (l, r, k) not in dp:
                res = float('inf')
                for i in range(l, r, K-1):
                    res = min(res, dfs(l, i, 1) + dfs(i+1, r, k-1))
                dp[l, r, k] = res
            return dp[l, r, k]
        
        res = dfs(0, len(stones)-1, 1)
        return res if res != float('inf') else -1