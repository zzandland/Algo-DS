class Solution {
public:
    int pathSum(vector<int>& nums) {
        vector<vector<int>> layer(4, vector<int>(8, -1));
        int d, p, v;
        for (int s: nums) {
            d = s / 100, p = s % 100 / 10, v = s % 10;
            layer[d-1][p-1] = v;
        }
        return dfs(layer, 0, 0, 0);
    }
    
    int dfs(vector<vector<int>>& layer, int d, int p, int sum) {
        if (layer[d][p] == -1) return 0;
        sum += layer[d][p];
        if (d == 3 || (layer[d+1][p*2] == -1 && layer[d+1][p*2+1] == -1)) return sum;
        return dfs(layer, d+1, p*2, sum) + dfs(layer, d+1, p*2+1, sum);
    }
};