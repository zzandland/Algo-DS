class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums, output = [lower-1] + nums + [upper+1], []
        for i, num in enumerate(nums):
            if num - nums[i-1] > 2: output.append('{}->{}'.format(nums[i-1]+1, num-1))
            elif num - nums[i-1] == 2: output.append(str(num-1))
        return output