#  Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

#  Example:

#  Input:
    #  [[0, 1, 1, 0, 1],
      #  [0, 1, 0, 1, 0],
      #  [0, 0, 0, 0, 1],
      #  [0, 1, 0, 0, 0]]

#  Output: 2

#  Explanation:
#  At the end of the 1st hour, the status of the grid:
    #  [[1, 1, 1, 1, 1],
      #  [1, 1, 1, 1, 1],
      #  [0, 1, 0, 1, 1],
      #  [1, 1, 1, 0, 1]]

#  At the end of the 2nd hour, the status of the grid:
    #  [[1, 1, 1, 1, 1],
      #  [1, 1, 1, 1, 1],
      #  [1, 1, 1, 1, 1],
      #  [1, 1, 1, 1, 1]]

def minHours(grid):
    if not grid: return -1
    r, c = len(grid), len(grid[0])
    q = [(i, j) for i in range(r) for j in range(c) if grid[i][j] == 1]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    time = 0
    while q:
        size = len(q)
        nq = []
        for (y, x) in q:
            for d in directions:
                ny, nx = y+d[0], x+d[1]
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == 0:
                    grid[ny][nx] = 1
                    nq.append((ny, nx))
        q = nq
        if not q: return time
        time += 1
    return time

grid = [[0, 1, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]]

print(minHours(grid))
