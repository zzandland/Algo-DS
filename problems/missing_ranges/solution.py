class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums = [lower-1] + nums + [upper+1]
        for i in range(len(nums)-1):
            l, u = nums[i]+1, nums[i+1]-1
            if l == u: res.append(str(l))
            elif l < u: res.append('%d->%d' % (l, u))
        return res