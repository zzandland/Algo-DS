class Solution {
public:
    int dfs(vector<int>& prices, int i, int mn) {
        if (i == prices.size()) return 0;
        int price = prices[i], newMn = min(mn, price);
        return max(price - newMn, dfs(prices, i + 1, newMn));
    }
    
    int maxProfit(vector<int>& prices) {
        return dfs(prices, 0, INT_MAX);
    }
};