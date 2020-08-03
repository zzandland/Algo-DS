class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return None
        m, n = len(image), len(image[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(y: int, x: int, c: int) -> None:
            for ny, nx in ((y+r, x+c) for r, c in directions):
                if 0 <= ny < m and 0 <= nx < n and image[ny][nx] == c:
                    image[ny][nx] = newColor
                    dfs(ny, nx, c)
        if image[sr][sc] != newColor:
            o = image[sr][sc]
            image[sr][sc] = newColor
            dfs(sr, sc, o)
        return image