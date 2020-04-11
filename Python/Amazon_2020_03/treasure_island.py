#  You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

#  Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

#  Example:

#  Input:
m = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]

#  Output: 5
#  Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

from typing import List
from collections import deque

def treasureIsland(map_: List[List[str]]) -> int:
    if not map_: return 0
    R, C = len(map_), len(map_[0])
    q, t, dir_ = deque([(0, 0)]), 0, [(1, 0), (-1, 0), (0, 1), (0, -1)]
    map_[0][0] = 'D'
    while q:
        t += 1
        l = len(q)
        for _ in range(l):
            y, x = q.popleft()
            for r, c in dir_:
                ny, nx = y+r, x+c
                if 0 <= ny < R and 0 <= nx < C:
                    if map_[ny][nx] == 'X': return t
                    if map_[ny][nx] == 'O':
                        map_[ny][nx] = 'D'
                        q.append((ny, nx))
    return -1

print(treasureIsland(m))
