class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest: return -1
        M, N = len(forest), len(forest[0])
        
        x = y = 0
        cnt = 1
        
        # prepare tree coords
        trees = sorted([(y, x) for y in range(M) for x in range(N) if forest[y][x] > 0], key=lambda x: forest[x[0]][x[1]])
        dir_ = (-1, 0, 1, 0, -1)
        
        def bfs(sy: int, sx: int, ty: int, tx: int) -> int:
            q = [(0, 0, sy, sx)]
            cost = {(sy, sx): 0}
            while q:
                f, g, y, x = heappop(q)
                if y == ty and x == tx: return g
                for ny, nx in ((y+r, x+c) for r, c in zip(dir_, dir_[1:])):
                    if 0 <= ny < M and 0 <= nx < N and forest[ny][nx]:
                        tmp = g + 1 + abs(ny-ty) + abs(nx-tx)
                        if tmp < cost.get((ny, nx), float('inf')):
                            cost[ny, nx] = tmp
                            heappush(q, (tmp, g+1, ny, nx))
            return -1
                    
        res = 0
        for ty, tx in trees:
            d = bfs(y, x, ty, tx)
            if d < 0: return -1
            res += d
            y, x = ty, tx
        return res