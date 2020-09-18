class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l, r = [1]*N, [1]*N
        run = 1
        for i in range(N):
            l[i] = run
            run *= nums[i]
        run = 1
        for i in range(N-1, -1, -1):
            r[i] = run
            run *= nums[i]
        return [a*b for a, b in zip(l, r)]