class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N, output = len(nums), set()
        nums.sort()
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, N-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    output.add((nums[i], nums[l], nums[r]))
                if s > 0: r -= 1
                else: l += 1
        return [list(triple) for triple in output]