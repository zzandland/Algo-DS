import bisect

class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        tmp = []
        for i, b in enumerate(bulbs, 1):
            l, r = 0, len(tmp)
            while l < r:
                m = l + (r-l)//2
                if b < tmp[m]: r = m
                else: l = m+1
            for n in tmp[l-(l>0):l+1]:
                if abs(b - n) - 1 == K: return i
            tmp.insert(l, b)
        return -1