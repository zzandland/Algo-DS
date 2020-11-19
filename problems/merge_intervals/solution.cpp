class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), 
        [](const vector<int> &a, const vector<int> &b) -> bool {
            return a[0] == b[0] ? a[1] < b[1] : a[0] < b[0];
        });
        
        vector<vector<int>> res;
        int s = intervals[0][0], e = intervals[0][1];
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] > e) {
                res.push_back(vector<int>{s, e});
                s = intervals[i][0], e = intervals[i][1];
            } else {
                e = max(e, intervals[i][1]);
            }
        }
        res.push_back(vector<int>{s, e});
        return res;
    }
};