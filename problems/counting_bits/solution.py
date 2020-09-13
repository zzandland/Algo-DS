class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0: return [0]
        res = [0, 1]
        for n in range(2, num+1):
            res.append(res[n & (n-1)] + 1)
        return res