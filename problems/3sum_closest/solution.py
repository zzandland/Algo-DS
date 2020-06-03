class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N, res = len(nums), float('inf')
        for i in range(N):
            d, l, r = target-nums[i], i+1, N-1
            while l < r:
                res = min(
                    res, nums[i]+nums[l]+nums[r], 
                    key=lambda x: abs(target-x)
                )
                if res == target: return res
                if nums[l]+nums[r] > d:
                    r -= 1
                else:
                    l += 1    
        return res