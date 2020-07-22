import bisect

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        changes = []
        for l, r, h in buildings:
            changes.append((l, h))
            changes.append((r, -h))
        changes.sort()
        heights = []
        prev = 0
        output = []
        for i, (idx, h) in enumerate(changes):
            if h > 0: bisect.insort_left(heights, h)
            if h < 0: heights.pop(bisect.bisect_left(heights, -h))
            if i < len(changes) - 1 and idx == changes[i+1][0]: continue
            if not heights: output.append((idx, 0))
            elif heights[-1] != prev:
                output.append((idx, heights[-1]))
                prev = heights[-1]
        return output