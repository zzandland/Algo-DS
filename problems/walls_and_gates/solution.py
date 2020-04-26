class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        R, C, INF = len(rooms), len(rooms[0]), 2147483647
        q, nq, d = {(y, x) for y in range(R) for x in range(C) if rooms[y][x] == 0}, set(), 0
        while q:
            d += 1
            for y, x in q:
                for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ny, nx = y+r, x+c
                    if 0 <= ny < R and 0 <= nx < C and rooms[ny][nx] == INF:
                        rooms[ny][nx] = d
                        nq.add((ny, nx))
            q, nq = nq, set()