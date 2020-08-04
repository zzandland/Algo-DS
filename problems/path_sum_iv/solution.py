class Solution:
    def pathSum(self, nums: List[int]) -> int:
        layer = [[-1]*8 for _ in range(4)]
        for s in nums:
            d, p, v = map(int, list(str(s)))
            layer[d-1][p-1] = v
            
        def dfs(d: int, p: int, sm: int) -> int:
            if layer[d][p] == -1: return 0
            sm += layer[d][p]
            if d == 3 or (layer[d+1][p*2] == -1 and layer[d+1][p*2+1] == -1): return sm
            return dfs(d+1, p*2, sm) + dfs(d+1, p*2+1, sm)
        return dfs(0, 0, 0)