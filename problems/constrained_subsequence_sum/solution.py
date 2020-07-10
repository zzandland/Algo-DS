from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque([(nums[0], 0)])
        res = nums[0]
        for i in range(1, len(nums)):
            while q[0][1] < i-k:
                q.popleft()
            cur = max(0, q[0][0]) + nums[i]
            res = max(res, cur)
            while q and q[-1][0] < cur:
                q.pop()
            q.append((cur, i))                
        return res