class Solution {
public:
    int lenLongestFibSubseq(vector<int>& A) {
        int N = A.size();
        unordered_map<int, int> index;
        for (int i = 0; i < N; ++i) index[A[i]] = i;
        
        map<pair<int, int>, int> dp;
        
        int res = 0;
        for (int k = 0; k < N; ++k) {
            for (int j = 0; j < k; ++j) {
                int diff = A[k] - A[j];
                if (index.count(diff) && index[diff] < j) {
                    dp[{j, k}] = dp[{index[diff], j}] + 1;
                    res = max(res, dp[{j, k}] + 2);
                }
            }
        }

        return res >= 3 ? res : 0;
    }
};