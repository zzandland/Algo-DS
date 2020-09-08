class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        l = r = 0
        while l < len(slots1) and r < len(slots2):
            if slots1[l][1] < slots2[r][0]: l += 1
            elif slots2[r][1] < slots1[l][0]: r += 1
            else:
                s = max(slots1[l][0], slots2[r][0])
                e = min(slots1[l][1], slots2[r][1])
                if e - s >= duration: return [s, s+duration]
                if slots1[l][0] < slots2[r][0]: l += 1
                else: r += 1
        return []