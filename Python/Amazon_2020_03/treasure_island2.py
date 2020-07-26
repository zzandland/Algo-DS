#  You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

#  Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

#  Example:

#  Input:
matrix = [['S', 'O', 'O', 'S', 'S'], ['D', 'O', 'D', 'O', 'D'], ['O', 'O', 'O', 'O', 'X'], ['X', 'D', 'D', 'O', 'O'], ['X', 'D', 'D', 'D', 'O']]

#  Output: 3
#  Explanation:
#  You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

from typing import List

def treasureIsland2(matrix: List[List[str]]) -> int:
    '''
    >>> treasureIsland2(matrix)
    3
    '''
    if not matrix: return -1
    M, N, dir_ = len(matrix), len(matrix[0]), [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 0

    # get all starting coords O(matrix)
    q = []
    for y in range(M):
        for x in range(N):
            if matrix[y][x] == 'S':
                matrix[y][x] = 'D'
                q.append((y, x))

    # bfs until any treasure is found O(matrix)
    while q:
        nq = []
        cnt += 1
        for y, x in q:
            for ny, nx in ((y+r, x+c) for r, c in dir_):
                if 0 <= ny < M and 0 <= nx < N:
                    if matrix[ny][nx] == 'X': return cnt
                    if matrix[ny][nx] == 'O':
                        matrix[ny][nx] = 'D'
                        nq.append((ny, nx))
        q = nq
    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
