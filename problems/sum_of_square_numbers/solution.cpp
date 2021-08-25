class Solution {
public:
    bool judgeSquareSum(int c) {
        int l = 0, r = (int)sqrt(c);
        while (l <= r) {
            int diff = c - l * l;
            if (diff == r * r) return true;
            if (diff > r * r) ++l;
            else --r;
        }
        return false;
    }
};