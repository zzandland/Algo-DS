class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # store all points into a set O(n)
        S = set(map(tuple, points))
        L = list(S)
        res = float('inf')
        # loop each point O(n) -> O(n^2)
        for i, (y1, x1) in enumerate(L):
            # loop points upto ith index O(n)
            for j in range(i):
                y2, x2 = L[j]
                # if the other coords are in set cal min area
                if y1 != y2 and x1 != x2 and (y1, x2) in S and (y2, x1) in S:
                    res = min(res, abs(y2-y1) * abs(x2-x1))
        return res if res != float('inf') else 0