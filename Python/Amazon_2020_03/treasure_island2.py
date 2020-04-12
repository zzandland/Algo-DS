#  You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

#  Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

#  Example:

#  Input:
matrix = [['S', 'O', 'O', 'S', 'S'], ['D', 'O', 'D', 'O', 'D'], ['O', 'O', 'O', 'O', 'X'], ['X', 'D', 'D', 'O', 'O'], ['X', 'D', 'D', 'D', 'O']]

#  Output: 3
#  Explanation:
#  You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

from typing import List
from collections import deque

def treasureIsland2(matrix: List[List[str]]) -> int:
    if not matrix: return -1
    R, C, dir_, d = len(matrix), len(matrix[0]), [(1, 0), (-1, 0), (0, 1), (0, -1)], 0
    q = deque()
    for y in range(R):
        for x in range(C):
            if matrix[y][x] == 'S':
                q.append((y, x))
                matrix[y][x] = 'D'
    while q:
        d+=1
        l = len(q)
        for _ in range(l):
            y, x = q.popleft()
            for r, c in dir_:
                ny, nx = y+r, x+c
                if 0 <= ny < R and 0 <= nx < C:
                    if matrix[ny][nx] == 'X': return d
                    elif matrix[ny][nx] == 'O':
                        q.append((ny, nx))
                        matrix[ny][nx] = 'D'
    return -1

print(treasureIsland2(matrix))
