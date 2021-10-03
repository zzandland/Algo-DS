class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int Y = dungeon.size(), X = dungeon[0].size();
        vector<vector<int>> dp(Y+1, vector<int>(X+1, INT_MAX));
        dp[Y][X-1] = dp[Y-1][X] = 1;
        for (int y = Y-1; y >= 0; --y) {
            for (int x = X-1; x >= 0; --x) {
                dp[y][x] = max(1, min(dp[y+1][x], dp[y][x+1]) - dungeon[y][x]);
            }
        }
       return dp[0][0];
    }
};
