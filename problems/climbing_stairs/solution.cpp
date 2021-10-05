class Solution {
public:
    int climbStairs(int n) {
        int f = 1, s = 1;
        while (--n > 0) {
            int t = f + s;
            f = s;
            s = t;
        }
        return s;
    }
};