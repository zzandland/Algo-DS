class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        int A = nums1.size(), B = nums2.size();
        unordered_map<int, vector<int>> pos;
        for (int i = 0; i < B; ++i) {
            if (!pos.count(nums2[i])) pos[nums2[i]] = vector<int>();
            pos[nums2[i]].push_back(i);
        }
        int res = 0;
        for (int i = 0; i < A; ++i) {
            for (int idx : pos[nums1[i]]) {
                int a = i, b = idx;
                while (nums1[a] == nums2[b] && a < A && b < B) ++a, ++b;
                res = max(res, b - idx);
                if (res >= A - i) {
                    cout << res;
                    return res;
                }
            }
        }
        return res;
    }
};