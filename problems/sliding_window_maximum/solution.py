from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i, n in enumerate(nums):
            while q and q[-1][0] < n: q.pop()
            q.append((n, i))
            if i >= k - 1:
                while q[0][1] <= i - k: q.popleft()
                res.append(q[0][0])
        return res