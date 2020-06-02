class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hor = sorted([0] + horizontalCuts + [h])
        ver = sorted([0] + verticalCuts + [w])
        hd = max([hor[i]-hor[i-1] for i in range(1, len(hor))])
        vd = max([ver[i]-ver[i-1] for i in range(1, len(ver))])
        return (hd * vd) % (10**9+7)