class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        res = []
        for i, num in enumerate(nums):
            heappush(q, (-num, i))
            while q[0][1] < i-k+1:
                heappop(q)
            if i >= k-1: res.append(-q[0][0])
        return res