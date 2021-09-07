class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        vector<int> times{0};
        times.insert(times.end(), releaseTimes.begin(), releaseTimes.end());
        string keys = "," + keysPressed;
        int mxT = 0;
        char res = ' ';
        for (int i = 1; i < times.size(); ++i) {
            int t = times[i] - times[i-1];
            char c = keys[i];
            if (mxT < t) {
                mxT = t;
                res = c;
            } else if (mxT == t && res < c) {
                res = c;
            }
        }
        return res;
    }
};