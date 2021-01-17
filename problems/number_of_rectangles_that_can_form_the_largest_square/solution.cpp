class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        int res, maxLen;
        res = maxLen = 0;
        for (auto rec : rectangles) {
            int m = min(rec[0], rec[1]);
            if (m == maxLen) {
                res++;
            } else if (m > maxLen) {
                maxLen = m;
                res = 1;
            }
        }
        return res;
    }
};