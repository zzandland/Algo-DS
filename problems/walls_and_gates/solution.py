from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return None
        R, C, cnt = len(rooms), len(rooms[0]), 0
        q, dir_ = deque([(y, x) for y in range(R) for x in range(C) if rooms[y][x] == 0]), [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            cnt += 1
            l = len(q)
            for _ in range(l):
                y, x = q.popleft()
                for r, c in dir_:
                    ny, nx = y+r, x+c
                    if 0 <= ny < R and 0 <= nx < C and rooms[ny][nx] == 2147483647:
                        rooms[ny][nx] = cnt
                        q.append((ny, nx))