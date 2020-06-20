class Solution:
    def nextPermutation(self, nums):
        N = len(nums)
        for i in range(N-1, 0, -1):
            if nums[i] > nums[i-1]:
                mni = min(filter(lambda x: nums[x] > nums[i-1], range(i, N)),
                          key=lambda x: nums[x])
                nums[i-1], nums[mni] = nums[mni], nums[i-1]
                nums[i:] = sorted(nums[i:])
                break
        else:
            nums.sort()