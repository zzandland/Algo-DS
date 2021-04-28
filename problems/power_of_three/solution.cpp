class Solution {
public:
    bool isPowerOfThree(int n) {
        while (n % 3 == 0 && n > 1) n /= 3;
        return n == 1;
    }
};