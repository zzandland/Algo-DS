class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        changes = []
        for i, j, k in bookings:
            changes.append((i-1, k))
            changes.append((j, -k))
        changes.sort()
        curr = prev = 0
        res = [0]*n
        for idx, change in changes:
            for i in range(prev, idx):
                res[i] = curr
            prev = idx
            curr += change
        return res