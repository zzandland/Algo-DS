class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        res = []
        l = r = nums[0]
        for i in range(1, len(nums)):
            if r != nums[i]-1:
                if l == r: res.append(str(l))
                else: res.append('%d->%d' % (l, r))
                l = r = nums[i]
            else:
                r = nums[i]
        if l == r: res.append(str(l))
        else: res.append('%d->%d' % (l, r))
        return res