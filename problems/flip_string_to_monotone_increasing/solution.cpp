class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int l0, l1, r0, r1;
        l0 = l1 = r0 = r1 = 0;
        for (char c : s) {
            if (c == '0') ++r0;
            else ++r1;
        }
        int res = l1 + r0;
        for (char c : s) {
            if (c == '0') {
                ++l0;
                --r0;
            } else {
                ++l1;
                --r1;
            }
            res = min(res, l1 + r0);
        }
        return res;
    }
};