class Solution {
public:
    int countArrangement(int n) {
        vector<bool> seen(n+1, false);
        return dfs(n, n, seen);
    }
    
    int dfs(int n, int i, vector<bool> &seen) {
        if (i == 0) return 1;
        int res = 0;
        for (int j = 1; j <= n; ++j) {
            if (!seen[j] && (i % j == 0 || j % i == 0)) {
                seen[j] = true;
                res += dfs(n, i-1, seen);
                seen[j] = false;
            }
        }
        return res;
    }
};