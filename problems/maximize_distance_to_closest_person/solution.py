class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if not seats: return 0
        if len(seats) == 1: return int(seats[0] == 0)
        ones = [i for i, s in enumerate(seats) if s == 1]
        N = len(ones)
        mx = ones[0]
        for i in range(1, N):
            mx = max(mx, (ones[i]-ones[i-1])//2)
        return max(mx, len(seats)-1-ones[-1])    