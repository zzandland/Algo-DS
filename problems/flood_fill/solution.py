class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if len(image) == 0:
            return image
        height, width = len(image), len(image[0])
        if not (0 <= sr < height and 0 <= sc < width and image[sr][sc] != newColor):
            return image
        q = collections.deque()
        q.append((sr, sc))
        origin_color = image[sr][sc]
        image[sr][sc] = newColor
        while len(q) > 0:
            row, col = q.popleft()
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if 0 <= r < height and 0 <= c < width and image[r][c] == origin_color:
                    image[r][c] = newColor
                    q.append((r, c))
        return image            