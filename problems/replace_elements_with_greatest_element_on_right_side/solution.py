class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res, mx = [], -1
        for n in arr[::-1]:
            res.append(mx)
            mx = max(mx, n)
        return res[::-1]