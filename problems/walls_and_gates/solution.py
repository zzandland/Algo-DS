class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        M, N = len(rooms), len(rooms[0])
        
        # find coords of doors O(rooms)
        q = [(y, x) for y in range(M) for x in range(N) if rooms[y][x] == 0]
        
        # increment distance in BFS O(rooms)
        dist = 1
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            nq = []
            for y, x in q:
                for ny, nx in ((y+r, x+c) for r, c in dir_):
                    if 0 <= ny < M and 0 <= nx < N and rooms[ny][nx] > dist:
                        rooms[ny][nx] = dist
                        nq.append((ny, nx))
            q = nq
            dist += 1