class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        res = 0
        prev = float('-inf')
        for i in range(N):
            if seats[i] == 1:
                if prev == float('-inf'): res = i
                else: res = max(res, (i - prev) // 2)
                prev = i
        return max(res, N-1 - prev)