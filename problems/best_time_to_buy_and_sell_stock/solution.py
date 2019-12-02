class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    buyPrice, maxPrice = float('inf'), 0
    for price in prices:
      if buyPrice > price:
        buyPrice = price
      elif maxPrice < price - buyPrice:
        maxPrice = price - buyPrice
    return maxPrice