class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        int sum = 0;
        for (int m : matchsticks) {
            sum += m;
        }
        if (sum % 4 != 0) return false;
        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
        vector<int> sides(4, 0);
        return dfs(sides, matchsticks, 0, sum / 4);
    }
    
    bool dfs(vector<int> &sides, vector<int> &matchsticks, int i, int side) {
        if (i == matchsticks.size()) {
            for (int j = 0; j < 4; ++j) {
                if (sides[j] != side) return false;
            }
            return true;
        }
        for (int j = 0; j < 4; ++j) {
            if (sides[j] + matchsticks[i] <= side) {
                sides[j] += matchsticks[i];
                if (dfs(sides, matchsticks, i+1, side)) return true;
                sides[j] -= matchsticks[i];
            }
        }
        return false;
    }
};