class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sm = sum(nums)
        if sm % k != 0: return False
        
        tmp = [sm // k] * k
        nums.sort(reverse=True)
        
        def dfs(i: int) -> bool:
            if i == len(nums): return True
            for j in range(len(tmp)):
                if tmp[j] >= nums[i]:
                    tmp[j] -= nums[i]
                    if dfs(i+1): return True
                    tmp[j] += nums[i]
            return False
        return dfs(0)