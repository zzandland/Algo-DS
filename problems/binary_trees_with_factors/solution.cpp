#define DIV 1000000007

class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        unordered_map<int, long> dp;
        sort(arr.begin(), arr.end());
        
        long res = 0;
        for (int n : arr) {
            long tmp = 1;
            for (int j = 0, a = arr[0]; a <= sqrt(n); a = arr[++j]) {
                if (n % a != 0) continue;
                int b = n / a;
                if (dp.count(b)) tmp += dp[a] * dp[b] * (a == b ? 1 : 2);
            }
            dp[n] = tmp;
            res = (res + tmp) % DIV;
        }
        return res;
    }
};