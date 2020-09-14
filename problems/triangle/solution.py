class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        for y in range(1, len(A)):
            for x in range(len(A[y])):
                val = A[y][x]
                A[y][x] = float('inf')
                if x > 0: A[y][x] = min(A[y][x], A[y-1][x-1] + val)
                if x < len(A[y]) - 1: A[y][x] = min(A[y][x], A[y-1][x] + val)
        return min(A[-1])