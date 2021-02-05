class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (int n : nums) freq[n]++;
        
        int res = 0;
        for (const auto &[n, f] : freq) {
            int b = freq.count(n-1) ? freq[n-1] : 0;
            int a = freq.count(n+1) ? freq[n+1] : 0;
            int tmp = max(b, a);
            if (tmp != 0) res = max(res, tmp + f);
        }
        return res;
    }
};