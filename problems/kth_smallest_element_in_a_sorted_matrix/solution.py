from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        q = [(-matrix[y].pop(), y) for y in range(N)]
        heapify(q)
        for _ in range(N*N-k+1):
            v, y = heappop(q)
            if matrix[y]: heappush(q, (-matrix[y].pop(), y))
        return -v