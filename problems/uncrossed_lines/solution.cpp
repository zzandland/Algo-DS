class Solution {
public:
    int maxUncrossedLines(vector<int>& A, vector<int>& B) {
        int dp[B.size()+1][A.size()+1];
        for (int i = 0; i < B.size()+1; ++i) fill_n(dp[i], A.size()+1, 0);
        
        for (int b = 0; b < B.size(); ++b) {
            for (int a = 0; a < A.size(); ++a) {
                int tmp = 0;
                if (A[a] == B[b]) tmp = 1 + dp[b][a];
                tmp = max(tmp, max(dp[b+1][a], dp[b][a+1]));
                dp[b+1][a+1] = tmp;
            }
        }
        
        return dp[B.size()][A.size()];
    }
};