class Solution {
public:
    int kthFactor(int n, int k) {
        vector<int> factors;
        for (int i = 1; i*i <= n; ++i) {
            if (n % i == 0) {
                if (i*i != n) factors.push_back(i);
                if (--k == 0) return i;
            }
        }
        return k > factors.size() ? -1 : n / factors[factors.size() - k];
    }
};