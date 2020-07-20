class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        define a state machine:
        1) we can only reach the state sold from selling the stock, thus previous
        state can be only sell (held + price of stock)
        2) we can reach the state held from either holding onto the stock or just
        buying the stock, thus previous actions are rest or buy (reset - price of stock)
        3) we can reach the state reset from either reset (no stock in hand) or just
        sold off stock, thus previous actions are rest
        """
        N = len(prices)
        # states: sold, held, reset
        sold = float('-inf') # at start we could not have just sold
        held = float('-inf') # at start we can't be holding onto a stock
        reset = 0
        res = 0
        # O(n)
        for price in prices:
            held = max(held, reset - price)
            reset = max(reset, sold)
            sold = held + price
        return max(sold, reset)