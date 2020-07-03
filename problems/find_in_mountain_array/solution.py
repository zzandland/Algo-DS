# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        L, R = 0, mountain_arr.length()-1
        def findPeak(l: int, r: int):
            while l < r:
                m = l + (r-l)//2
                mid, nxt = mountain_arr.get(m), mountain_arr.get(m+1)
                if mid > nxt:
                    if mid > mountain_arr.get(m-1): return m
                    else: r = m
                else: l = m+1
            return l
        def findVal(l: int, r: int, asc: bool):
            while l <= r:
                m = l + (r-l)//2
                mid = mountain_arr.get(m)
                if mid == target: return m
                if mid < target:
                    if asc: l = m+1
                    else: r = m-1
                else:
                    if asc: r = m-1
                    else: l = m+1
            return -1
        peak = findPeak(L, R)
        lf = findVal(L, peak, True)
        if lf != -1: return lf
        return findVal(peak+1, R, False)