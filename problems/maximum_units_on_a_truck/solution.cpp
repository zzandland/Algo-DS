class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        priority_queue<int> pq;
        sort(boxTypes.begin(), boxTypes.end(), [&](auto &a, auto &b) {
            return a[1] > b[1];
        });
        int res = 0;
        for (auto &s : boxTypes) {
            while (truckSize > 0 && s[0]-- > 0) {
                res += s[1];
                --truckSize;
            }
        }
        return res;
    }
};