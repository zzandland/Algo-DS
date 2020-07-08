class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
            rem = -num
            l, r = i+1, N-1
            seen = set()
            while l < r:
                sm = nums[l] + nums[r]
                if sm == rem and (nums[l], nums[r]) not in seen:
                    res.append([num, nums[l], nums[r]])
                    seen.add((nums[l], nums[r]))
                if sm < rem: l += 1
                else: r -= 1
        return res