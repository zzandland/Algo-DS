class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 3 states:
        # 1. free: come from sold last turn (sold[i-1]) or resting (free[i-1])
        # 2. sold: come from selling (held[i-1] + prices[i])
        # 3. held: come from free (free[i-1] - prices[i] - fee) or resting (held[i-1]) or buy after sell (sold[i-1] - prices[i] - fee)
        # initially you can only be at 'free' state
        free, sold, held = 0, float('-inf'), float('-inf')
        for price in prices:
            total = price + fee
            free = max(sold, free)
            held = max(free - total, held, sold - total)
            sold = held + price
        return max(free, sold)