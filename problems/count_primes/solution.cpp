class Solution {
public:
  int countPrimes(int n) {
    vector<bool> not_prime(n);
    int count = 0;
    for (size_t i = 2; i < n; ++i) {
      if (!not_prime[i]) {
        count++;
        for (size_t j = 2; i * j < n; ++j) {
          not_prime[i * j] = true;
        }
      }
    }
    return count;
  }
};