class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        mx = step = cnt = 0
        if N == 1: return 0
        for i, num in enumerate(nums):
            mx = max(mx, num+i)
            if i == step:
                step, cnt = mx, cnt+1
                if step >= N-1: return cnt
        return cnt