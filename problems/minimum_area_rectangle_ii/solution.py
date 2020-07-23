from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # save all coords into a set O(n)
        st = set(map(tuple, points))
        res = float('inf')
        diag_dic = defaultdict(set)
        
        # O(n^2)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                y1, x1 = points[i]
                y2, x2 = points[j]
                # check for rectangle that is parallel to y and x
                if y1 != y2 and x1 != x2 and (y1, x2) in st and (y2, x1) in st:
                    res = min(res, abs(y2-y1) * abs(x2-x1))
                else:
                    if y1 > y2: y1, y2, x1, x2 = y2, y1, x2, x1
                    # check for diagonal rectangles
                    for y3, x3, y4, x4 in diag_dic[y2-y1, x2-x1]:
                        if len(set([(y1, x1), (y2, x2), (y3, x3), (y4, x4)])) == 4:
                            a = abs(y2-y1)**2 + abs(x2-x1)**2
                            b = abs(y4-y2)**2 + abs(x4-x2)**2
                            c = abs(y4-y1)**2 + abs(x4-x1)**2
                            if a + b == c:
                                res = min(res, sqrt(a) * sqrt(b))
                    diag_dic[y2-y1, x2-x1].add((y1, x1, y2, x2))
        return res if res != float('inf') else 0