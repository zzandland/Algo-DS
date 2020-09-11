class Solution:
    def splitArray(self, nums: List[int], M: int) -> int:
        def check(t: int) -> int:
            cnt = 1
            sm = 0
            for n in nums:
                if sm + n > t:
                    cnt += 1
                    sm = n
                else: sm += n
            return cnt
        l, r = max(nums), sum(nums)
        while l < r:
            m = l + (r-l)//2
            if check(m) <= M: r = m
            else: l = m+1
        return l