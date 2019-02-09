class Solution {
  public int maxProfit(int[] prices) {
    int bought = Integer.MAX_VALUE;
    int max = 0;
    for (int price : prices) {
      if (bought > price) bought = price;
      else {
        int profit = price - bought;
        if (profit > max) max = profit;
      }
    }
    return max;
  }
}