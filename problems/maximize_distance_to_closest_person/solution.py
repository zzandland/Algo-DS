class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_len, pre = 0, None
        for i, seat in enumerate(seats):
            if seat == 1:
                if pre is None:
                    max_len = i
                else:
                    max_len = max(max_len, (i - pre) // 2)
                pre = i    
        return max(max_len, len(seats) - 1 - pre)        