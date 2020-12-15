class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res;
        int l = 0, r = nums.size()-1;
        while (l <= r) {
            int ls = nums[l] * nums[l];
            int rs = nums[r] * nums[r];
            if (ls < rs) {
                res.push_back(rs);
                r--;
            } else {
                res.push_back(ls);
                l++;
            }
        }
        
        for (int i = 0; i < res.size() / 2; ++i) {
            int tmp = res[i];
            res[i] = res[res.size()-1-i];
            res[res.size()-1-i] = tmp;
        }
        
        return res;
    }
};