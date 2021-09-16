class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        if (arr.size() == 0) return 0;
        int prev = arr[0], res = 0, tmp = 1;
        bool up = false, first = true;
        for (int i = 1; i < arr.size(); ++i) {
            if (first) {
                if (prev != arr[i]) {
                    up = prev < arr[i];
                    ++tmp;
                    first = false;
                }
            } else {
                if (prev == arr[i]) {
                    res = max(res, tmp);
                    tmp = 1;
                    first = true;
                } else {
                    bool nxt = prev < arr[i];
                    if (up == nxt) {
                        res = max(res, tmp);
                        tmp = 2;
                    } else {
                        ++tmp;
                    }
                    up = nxt;
                }
            }
            prev = arr[i];
        }
        return max(res, tmp);
    }
};