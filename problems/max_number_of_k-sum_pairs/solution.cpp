class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> dic;
        int res = 0;
        for (int n : nums) {
            int r = k - n;
            if (dic[n]) {
                res++;
                dic[n]--;
            } else {
                dic[r]++;
            }
        }
        return res;
    }
};