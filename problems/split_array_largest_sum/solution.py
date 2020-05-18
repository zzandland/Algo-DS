class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split(n: int) -> int:
            cnt, run = 1, 0
            for num in nums:
                if num + run <= n: run += num
                else:
                    run, cnt = num, cnt+1
            return cnt    
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r-l)//2
            if split(mid) <= m: r = mid
            else: l = mid+1
        return l        