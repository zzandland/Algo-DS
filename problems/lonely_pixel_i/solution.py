from collections import Counter

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture: return 0
        N, M = len(picture), len(picture[0])
        rows, cols = [0]*N, [0]*M
        for y, row in enumerate(picture):
            for x, _ in enumerate(row):
                if picture[y][x] == 'B':
                    rows[y] += 1
                    cols[x] += 1
        res = 0
        for y, row in enumerate(picture):
            for x, _ in enumerate(row):
                if picture[y][x] == 'B' and rows[y] == 1 and cols[x] == 1:
                    res += 1
        return res