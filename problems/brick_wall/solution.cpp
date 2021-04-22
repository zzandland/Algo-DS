class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        int res, mn, i, tmp, newmn;
        res = mn = INT_MAX;
        for (const auto &w : wall) {
            mn = min(mn, w[w.size() - 1]);
        }
        i = 0;
        for (bool done = false; !done; ++i) {
            tmp = 0, newmn = INT_MAX;
            for (auto &w : wall) {
                if (w[w.size() - 1] - mn == 0) {
                    w.pop_back();
                    if (w.empty()) {
                        done = true;
                        break;
                    }
                } else {
                    w[w.size() - 1] -= mn;
                    ++tmp;
                }
                newmn = min(newmn, w[w.size() - 1]);
            }
            if (!done) res = min(res, tmp);
            mn = newmn;
        }
        return i == 1 ? wall.size() : res;
    }
};