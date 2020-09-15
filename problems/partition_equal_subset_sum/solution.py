class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        N = len(nums)
        if sm % 2 != 0: return False
        
        @functools.lru_cache(None)
        def dfs(i: int, t: int) -> bool:
            if t < 0: return False
            if t == 0: return True
            if i == N: return False
            return dfs(i+1, t - nums[i]) or dfs(i+1, t)
        
        return dfs(0, sm / 2)