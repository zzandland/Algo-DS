from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        idx = defaultdict(list)
        for i, n in enumerate(arr):
            if 0 < i < N-1 and arr[i-1] == arr[i] == arr[i+1]: continue
            idx[n].append(i)
        q = [(0, 0)]
        seen = {0: 0}
        while q:
            c, i = heappop(q)
            if -i == N-1: return c
            tmp = idx[arr[-i]] + [-i-1, -i+1]
            for j in tmp:
                if 0 <= j < N and j != -i:
                    if j not in seen or seen[j] > c:
                        seen[j] = c
                        heappush(q, (c+1, -j))
        return -1