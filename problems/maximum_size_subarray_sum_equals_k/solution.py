class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: -1}
        run = res = 0
        for i, n in enumerate(nums):
            run += n
            if run-k in seen: res = max(res, i - seen[run-k])
            if run not in seen: seen[run] = i
        return res