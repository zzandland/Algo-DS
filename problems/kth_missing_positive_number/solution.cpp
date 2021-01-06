class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int t = 1;
        for (int n : arr) {
            if (k <= n - t) return t + k - 1;
            k -= (n - t);
            t = n + 1;
        }
        return t + k - 1;
    }
};