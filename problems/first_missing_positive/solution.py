class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        def dfs(i: int) -> None:
            if not (0 < i <= N) or nums[i-1] == i: return
            tmp = nums[i-1]
            nums[i-1] = i
            dfs(tmp)
        for i in range(N):
            dfs(nums[i])
        for i in range(N):
            if nums[i] != i+1: return i+1
        return N+1