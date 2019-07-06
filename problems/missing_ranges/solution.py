class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        output = []
        if len(nums) == 0:
            l, r = lower, upper
            tmp = str(l) + '->' + str(r) if l != r else str(l)
            output.append(tmp)
            return output
        if lower != nums[0]:
            l, r = lower, nums[0] - 1
            tmp = str(l) + '->' + str(r) if l != r else str(l)
            output.append(tmp)
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] > 1:
                l, r = nums[i] + 1, nums[i+1] - 1
                tmp = str(l) + '->' + str(r) if l != r else str(l)
                output.append(tmp)
        if upper != nums[-1]:
            l, r = nums[-1] + 1, upper
            tmp = str(l) + '->' + str(r) if l != r else str(l)
            output.append(tmp)
        return output            