class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        if (A.size() < 3) return 0;
        int ln = 2;
        int diff = A[1] - A[0];
        int res = 0;
        for (int i = 2; i < A.size(); ++i) {
            int cur = A[i] - A[i-1];
            if (cur == diff) {
                ln++;
                res += ln - 2;
            } else {
                ln = 2;
                diff = cur;
            }
        }
        return res;
    }
};