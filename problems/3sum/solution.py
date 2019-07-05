class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output, dup = [], set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            diff = -1 * nums[i]
            while l < r:
                if nums[l] + nums[r] == diff and (nums[i], nums[l], nums[r]) not in dup: 
                    output.append([nums[i], nums[l], nums[r]])
                    dup.add((nums[i], nums[l], nums[r]))
                if nums[l] + nums[r] < diff:
                    l += 1
                else:
                    r -= 1    
        return output            