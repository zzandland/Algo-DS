class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        left = 0
        while numBottles > 0:
            res += numBottles
            numBottles, left = divmod(numBottles + left, numExchange)
        return res