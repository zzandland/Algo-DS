class Solution {
public:
    vector<int> constructArray(int n, int k) {
        // 1 2 3 4 5 6
        // 3 1 2 4 5 6
        // 4 1 3 2 5 6
        // 5 1 4 2 3 6
        // 6 1
        vector<int> res(n, 0);
        for (int i = 1; i <= n; ++i) res[i-1] = i;
        int l = 1, r = k + 1, i = 0;
        while (l < r) {
            res[i++] = l++;
            res[i++] = r--;
        }
        if (l == r) res[i] = l;
        return res;
    }
};