class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        if (left == right) return left;
        int res = 0;
        while (left > 0) {
            int digit = 0, cpy = left;
            while (cpy > 0) {
                ++digit;
                cpy >>= 1;
            }
            if (right >= pow(2, digit)) return res;
            res += (1 << (digit - 1));
            left &= ~(1 << (digit - 1));
            right &= ~(1 << (digit - 1));
        }
        return res;
    }
};

// 110
// 111
