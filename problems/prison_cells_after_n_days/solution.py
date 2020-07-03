class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        L = len(cells)
        def transform(c: List[int]) -> List[int]:
            res = [0]*L
            for i in range(1, L-1):
                res[i] = int(not(c[i-1] != c[i+1]))
            return res
        N = 14 if N % 14 == 0 else N % 14
        for _ in range(N):
            cells = transform(cells)
        return cells