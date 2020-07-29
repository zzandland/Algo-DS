class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state machine
        # free state from taking break (free) or just sold a stock (sold)
        # sold state from selling (held+price)
        # held state from taking break (free) or buying after cooldown (free-price)
        
        free, sold, held = 0, float('-inf'), float('-inf')
        
        for price in prices:
            held = max(held, free-price)
            free = max(free, sold)
            sold = held+price
            
        return max(free, sold)