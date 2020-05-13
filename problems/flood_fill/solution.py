from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return None
        R, C = len(image), len(image[0])
        q, prev = deque([(sr, sc)]), image[sr][sc]
        if prev == newColor: return image
        while q:
            y, x = q.popleft()
            image[y][x] = newColor
            for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y+r, x+c
                if 0 <= ny < R and 0 <= nx < C and image[ny][nx] == prev: q.append((ny, nx))
        return image            