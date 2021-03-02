class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int seen[nums.size() + 1];
        for (int i = 0; i <= nums.size(); ++i) seen[i] = 0;
        for (int n : nums) seen[n]++;
        vector<int> res(2);
        for (int i = 1; i <= nums.size(); ++i) {
            int n = seen[i];
            if (n == 0) res[1] = i;
            else if (n == 2) res[0] = i;
        }
        return res;
    }
};