from collections import deque
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N, idx = len(arr), bisect.bisect_left(arr, x)
        l = r = idx
        while l >= 0 and r < N and r-l-1 < k:
            if abs(arr[l]-x) <= abs(arr[r]-x): l -= 1
            else: r += 1
        if l == -1: return arr[:k]
        if r == N: return arr[N-k:]
        return arr[l+1:r]