class Solution {
  public int maxProfit(int[] prices) {
    boolean bought = false;
    int initial = 0;
    int profit = 0;
    for (int i = 0; i < prices.length - 1; i++) {
      if (!bought && prices[i] < prices[i + 1]) {
        bought = true;
        initial = prices[i];
      } else if (bought && prices[i] > prices[i + 1]) {
        bought = false;
        profit += prices[i] - initial;
      }
    }
    if (bought) profit += prices[prices.length - 1] - initial;
    return profit;
  }
}