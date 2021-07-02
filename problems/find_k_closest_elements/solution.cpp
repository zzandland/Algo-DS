class Solution {
public:
    int bs(vector<int> &arr, int x) {
        int l = 0, r = arr.size() - 1;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (arr[m] < x) l = m +1;
            else r = m;
        }
        return l;
    }
    
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int l = bs(arr, x), r = l, len = arr.size();
        while (0 <= l && r < len && r - l <= k) {
            if (abs(arr[l] - x) > abs(arr[r] - x)) {
                ++r;
            } else {
                --l;
            }
        }
        while (0 <= l && r - l <= k) --l;
        while (r < len && r - l <= k) ++r;
        vector<int> res(arr.begin() + l + 1, arr.begin() + r);
        return res;
    }
};