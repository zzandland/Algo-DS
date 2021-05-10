class Solution {
public:
    int countPrimes(int n) {
        vector<bool> sieve(n-2, true);
        int res = 0;
        for (int i = 2; i < n; ++i) {
            if (sieve[i-2]) {
                ++res;
                for (int j = 2; i * j < n; ++j) {
                    sieve[i*j-2] = false;
                }
            }
        }
        return res;
    }
};