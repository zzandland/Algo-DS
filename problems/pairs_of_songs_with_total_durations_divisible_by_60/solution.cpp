class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int rems[60] = { 0 };
        int res = 0;
        for (int t : time) {
            int mod = t % 60;
            res += rems[mod == 0 ? 0 : 60 - mod];
            rems[mod]++;
        }
        return res;
    }
};