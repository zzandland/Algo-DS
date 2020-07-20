class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        define state machine
        1) sold -> only from selling stock (held + price)
        2) held 
            a) from buying stock right after selling (sold - price - fee)
            b) from buying stock from reset (reset - price - fee)
            c) from holdiing onto stock (held)
        3) reset
            a) from resting (reset)
            b) from just sold stock (sold)
        """
        # initial state can only be reset
        reset, sold, held = 0, float('-inf'), float('-inf')
        for price in prices:
            held = max(sold - price - fee, reset - price - fee, held)
            reset = max(reset, sold)
            sold = held + price
        return max(reset, sold)