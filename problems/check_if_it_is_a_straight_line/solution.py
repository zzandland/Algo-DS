class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        L = len(coordinates)
        for i in range(1, L):
            y1, x1 = coordinates[i]
            y2, x2 = coordinates[i-1]
            d1 = (y1-y2)//(x1-x2) if x1-x2 != 0 else 0
            if i > 1 and d1 != d2: return False
            d2 = d1
        return True    