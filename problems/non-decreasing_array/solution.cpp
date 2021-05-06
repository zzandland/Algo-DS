class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int min, prev;
        min = prev = INT_MIN;
        bool changed = false;
        for (int n : nums) {
            if (min > n) {
                if (changed) return false;
                changed = true;
                if (n >= prev) min = n;
            } else {
                prev = min;
                min = n;
            }
        }
        return true;
    }
};