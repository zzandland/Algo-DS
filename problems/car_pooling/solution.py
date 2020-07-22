class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = []
        for p, s, e in trips:
            changes.append((s, p))
            changes.append((e, -p))
        changes.sort()
        curr = 0
        for _, change in changes:
            curr += change
            if curr > capacity: return False
        return True