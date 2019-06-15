class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if not prices:
            return profit
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > profit:
                profit = prices[i] - lowest    
        return profit        